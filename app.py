import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Streamlit Website",
    page_icon="🌐",
    layout="centered"
)

# Custom CSS (optional)
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main content
st.title("🌟 Welcome to My Streamlit Website")
st.subheader("Built entirely with Python and Streamlit")

st.write("""
This is a simple homepage to get you started. Use the sidebar to navigate to other pages like **About**, **Projects**, or **Contact**.
""")

# Optional image (make sure the path is correct)
st.image("assets/logo.png", width=150, caption="Your Logo")

# Expandable section
with st.expander("📌 More Info"):
    st.markdown("""
    - This site is interactive and easy to customize.
    - You can add charts, forms, and even machine learning models.
    - Check out the other pages to see more!
    """)
