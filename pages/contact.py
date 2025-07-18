import streamlit as st

st.set_page_config(page_title="Contact", layout="centered")
st.title("📬 Contact Us")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    message = st.text_area("How can we help you?")
    submitted = st.form_submit_button("Send")

if submitted:
    st.success("✅ Thanks! We'll follow up shortly.")

# --- DEBUG: See all valid page names ---
try:
    from streamlit.source_util import get_pages

    st.divider()
    st.subheader("🛠 Debug: Valid switch_page() targets")

    pages = get_pages("")
    for page in pages.values():
        st.write(f"- `{page['page_name']}` → `st.switch_page('{page['page_name']}')`")

except Exception as e:
    st.error(f"Debug failed: {e}")
