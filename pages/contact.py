import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages

_on_pages_changed()
pages = get_pages("")

st.write("Available pages:")
for page in pages.values():
    st.write(f"- {page['page_name']}")

st.title("📬 Contact Us")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    message = st.text_area("How can we help you?")
    submitted = st.form_submit_button("Send")

if submitted:
    st.success("✅ Thanks! We'll follow up shortly.")

