# 💸 Expense Management System

An end-to-end Expense Management System built using **FastAPI** for the backend and **Streamlit** for the frontend. This system allows users to add, edit, delete expenses, and generate real-time analytics.

## 📁 Project Structure

expense-management-system/
├── frontend/ # Streamlit app code
├── backend/ # FastAPI server code
├── tests/ # Unit tests for backend and frontend
├── requirements.txt # Python dependencies
└── README.md # Project overview and setup instructions

## 🚀 Features

- Add/Edit/Delete expense transactions
- Real-time monthly reports and dashboards
- Category-wise and month-wise analytics with percentage breakdowns
- RESTful backend API using FastAPI
- Interactive UI using Streamlit

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/souro/expense-management-system.git
cd expense-management-system
pip install -r requirements.txt
uvicorn server.server:app --reload
streamlit run frontend/app.py
pytest tests/

Let me know if you want this README to include a screenshot, demo GIF, or deployment guide (like Docker or Render).
