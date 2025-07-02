import streamlit as st
import streamlit_authenticator as stauth

from add_update_ui import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_month import analytics_months_tab

# --- Step 1: Hash passwords (For development/testing only) ---
passwords = ['123', '456']
import streamlit_authenticator as stauth
hashed = stauth.Hasher(['your-password']).generate()
print(hashed)
print("Hashed passwords:", hashed_passwords)

# --- Step 2: Define user credentials ---
names = ['Alice', 'Bob']
usernames = ['alice', 'bob']

# --- Step 3: Use hashed passwords from above ---
# ⚠️ In production, use pre-generated hashed_passwords and remove line 8–9
credentials = {
    "usernames": {
        usernames[i]: {
            "name": names[i],
            "password": hashed_passwords[i]
        } for i in range(len(usernames))
    }
}

# --- Step 4: Create authenticator instance ---
authenticator = stauth.Authenticate(
    credentials,
    "expense_app",      # cookie name
    "auth_key",         # signature key
    cookie_expiry_days=1
)

# --- Step 5: Login form ---
name, authentication_status, username = authenticator.login("Login", "main")

# --- Step 6: Show app after login ---
if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {name} 👋")

    st.title("Expense Tracking System")

    tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months"])
    with tab1:
        add_update_tab()
    with tab2:
        analytics_category_tab()
    with tab3:
        analytics_months_tab()

elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")
