import streamlit as st
import os

st.divider()
st.subheader("🛠 Manual Page Debug")

# List files in the pages folder
pages_dir = "pages"
if os.path.exists(pages_dir):
    pages = [f for f in os.listdir(pages_dir) if f.endswith(".py")]
    for p in pages:
        st.write(f"🧾 Found file: `{p}` → `st.switch_page('{os.path.splitext(p)[0]}')`")
else:
    st.error("⚠️ Could not find the 'pages' directory.")
