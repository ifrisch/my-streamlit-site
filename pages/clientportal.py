import streamlit as st

st.set_page_config(page_title="Client Portal", layout="centered")
st.title("clientportal)")

# --- Auth check ---
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("🚫 You must be logged in to access the portal.")
    st.stop()

# --- Welcome Message ---
st.success(f"✅ Welcome, {st.session_state.user_email}!")

# --- Upload Section ---
st.subheader("📁 Upload Documents")
uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "xlsx"])
if uploaded_file:
    st.success(f"✅ File '{uploaded_file.name}' uploaded successfully.")
    # Placeholder — implement file saving later

# --- Status Section ---
st.subheader("📝 Current Status")
st.info("Your tax documents are under review. We’ll notify you once they're ready!")

# --- Logout Button ---
if st.button("🚪 Logout"):
    st.session_state.clear()
    st.experimental_rerun()
