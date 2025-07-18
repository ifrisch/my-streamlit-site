import streamlit as st
import pandas as pd
import hashlib
import os
from streamlit_extras.switch_page_button import switch_page  # ✅ NEW import

# --- Configuration ---
USER_DB = "user_database.csv"

# --- Create empty user DB if it doesn't exist ---
if not os.path.exists(USER_DB):
    df = pd.DataFrame(columns=["email", "name", "password_hash"])
    df.to_csv(USER_DB, index=False)

users_df = pd.read_csv(USER_DB)

# --- Hashing function ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- Page UI ---
st.set_page_config(page_title="New Client Registration", layout="centered")
st.title("📝 New Client Registration")

with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")
    submitted = st.form_submit_button("Register")

if submitted:
    if password != confirm:
        st.error("❌ Passwords do not match.")
    elif email in users_df["email"].values:
        st.error("❌ Email already registered.")
    else:
        new_user = {
            "email": email,
            "name": name,
            "password_hash": hash_password(password)
        }
        new_row = pd.DataFrame([new_user])
        users_df = pd.concat([users_df, new_row], ignore_index=True)
        users_df.to_csv(USER_DB, index=False)

        st.session_state.logged_in = True
        st.session_state.user_email = email

        st.success("✅ Registration successful. Redirecting to your portal...")
        switch_page("Client Portal")  # ✅ Now using streamlit-extras
