import streamlit as st

st.set_page_config(
    page_title="GridGuard AI",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ GridGuard AI")

st.success("Smart Grid Monitoring System")

# Dashboard Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Grid Status", "Healthy")

with col2:
    st.metric("Substations", 4)

with col3:
    st.metric("Availability", "100%")

st.divider()

if st.button("🚨 Inject Fault"):

    st.error("⚠ Fault Detected: B-C")

    st.subheader("Alternative Route")

    st.write("A → D → C")

    st.success("✅ Power Restored")