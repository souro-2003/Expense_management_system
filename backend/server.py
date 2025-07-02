from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Expense(BaseModel):
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):
    start_date: date
    end_date: date


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database.")

    return expenses


@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Expenses updated successfully"}


@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    # Fetch data from the database
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)

    # Check if data is None or empty
    if not data:
        raise HTTPException(status_code=500, detail="No expense data found for the given date range.")

    try:
        # Calculate the total amount, defaulting to 0 for missing keys
        total = sum(row.get('total', 0) for row in data)

        # Build the breakdown dictionary
        breakdown = {}
        for row in data:
            category = row.get('category', 'Unknown')  # Default to 'Unknown' if 'category' is missing
            row_total = row.get('total', 0)  # Default to 0 if 'total' is missing
            percentage = (row_total / total) * 100 if total != 0 else 0
            breakdown[category] = {
                "total": row_total,
                "percentage": percentage
            }
        return breakdown
    except Exception as e:
        # Log the error for debugging
        print(f"Error processing analytics data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error while processing analytics.")

@app.get("/monthly_summary/")
def get_analytics():
    monthly_summary = db_helper.fetch_monthly_expense_summary()
    if monthly_summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve monthly expense summary from the database.")

    return monthly_summary
