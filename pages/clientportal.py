import streamlit as st

# --- USER DATABASE (TEMPORARY IN-CODE) ---
users = {
    "client1@example.com": "password123",
    "client2@example.com": "abc456"
}

# --- LOGIN FORM ---
st.title("🔐 Client Portal Login")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if email in users and users[email] == password:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.success("✅ Login successful")
                st.experimental_rerun()
            else:
                st.error("❌ Incorrect email or password")
else:
    st.success(f"Welcome, {st.session_state.user_email}!")
    
    # --- Secure Client Area Below ---
    st.subheader("📁 Your Documents")
    st.write("⬇️ Download, upload, or view your current tax documents.")

    uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "xlsx"])
    if uploaded_file:
        st.success("✅ File uploaded!")

    st.button("🚪 Logout", on_click=lambda: st.session_state.clear())
