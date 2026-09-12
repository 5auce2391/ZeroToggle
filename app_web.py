# app_web.py
import streamlit as st
import os

st.set_page_config(page_title="Standalone Smart Home App", layout="centered")
st.title("🏡 Standalone Smart Home App")

if os.path.exists("refactored_app.py"):
    import refactored_app as app_module

    temperature = st.slider("Current Temperature (°F)", 60, 90, 75)

    if st.button("Run Smart Home Routine"):
        try:
            output = app_module.run_smart_home_routine(temperature)
            st.success(f"Execution Successful:\n\n{output}")
        except Exception as e:
            st.error(f"Execution Error / Feature Blocked: {e}")
else:
    st.warning("Please run the AI Refactor from the ZeroToggle dashboard first to generate `refactored_app.py`.")
