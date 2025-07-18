import streamlit as st

st.set_page_config(page_title="Contact", layout="centered")
st.title("📬 Contact Us")

# Dummy form (keep your original)
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    message = st.text_area("How can we help you?")
    submitted = st.form_submit_button("Send")

if submitted:
    st.success("✅ Thanks! We'll follow up shortly.")

# --- TEMP: Show what pages are clickable
st.subheader("Debug: Try switching pages")

try:
    # Hardcode known options or guess a few
    possible_pages = ["Client Portal", "Clientportal", "clientportal", "New Client Registration", "Newclientregistration"]
    page_choice = st.radio("Try switching to:", possible_pages)

    if st.button("Switch to page"):
        st.switch_page(page_choice)

except Exception as e:
    st.error(f"⚠️ switch_page failed: {e}")
