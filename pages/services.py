import streamlit as st

st.title("💼 Services")
st.write("Explore our core CPA services designed to simplify your financial life:")

cols = st.columns(2)

with cols[0]:
    st.subheader("🧾 Tax Preparation")
    st.write("• Individuals (1040s)\n• Small businesses\n• Multi-state returns")

with cols[1]:
    st.subheader("📊 Bookkeeping")
    st.write("• Monthly/quarterly packages\n• QuickBooks setup\n• Reconciliations")

with cols[0]:
    st.subheader("📈 Tax Planning")
    st.write("• Proactive strategies\n• Entity structure analysis\n• Quarterly reviews")

with cols[1]:
    st.subheader("👨‍💼 Fractional CFO")
    st.write("• Financial oversight\n• Cash flow planning\n• Investor readiness")
