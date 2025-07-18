import streamlit as st
import pandas as pd
import os
import hashlib

# --- Password hashing ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- File path to store user data ---
USER_DB = "data/users.csv"

# --- Create data/users.csv if it doesn't exist ---
if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.isfile(USER_DB):
    df = pd.DataFrame(columns=["email", "name", "password_hash"])
    df.to_csv(USER_DB, index=False)

# --- Load existing users ---
users_df = pd.read_csv(USER_DB)

# --- UI ---
st.title("📝 New Client Registration")

with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
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
          
            st.success("✅ Registration successful. Logging you in...")
            st.stop()  # prevent the script from continuing this round

            st.markdown(
            '<meta http-equiv="refresh" content="1; url=/ClientPortal">',
            unsafe_allow_html=True
        )
            st.stop()