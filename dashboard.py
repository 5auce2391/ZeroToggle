# dashboard.py
import streamlit as st
import json
import os
import main

st.set_page_config(page_title="ZeroToggle Control Plane", layout="wide")
st.title("⚡ ZeroToggle - Feature Flag Control Plane")

if "flags" not in st.session_state:
    st.session_state.flags = {}

def save_flags_to_disk():
    with open("flags.json", "w") as f:
        json.dump(st.session_state.flags, f)

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Clean Source Code")
    if os.path.exists("app_code.py"):
        with open("app_code.py", "r") as f:
            st.code(f.read(), language="python")

    if st.button("🚀 Run Autonomous AI Refactor"):
        with st.spinner("Refactoring & validating..."):
            with open("app_code.py", "r") as f:
                source_code = f.read()
            result = main.run_zero_toggle(source_code)
            st.session_state.flags = {flag: False for flag in result["detected_flags"]}
            save_flags_to_disk()
            st.success("Refactoring complete! `refactored_app.py` created.")
            st.rerun()

with col_right:
    st.subheader("Real-Time Toggle Control Center")
    if os.path.exists("refactored_app.py"):
        with open("refactored_app.py", "r") as f:
            st.code(f.read(), language="python")

        st.divider()
        if st.session_state.flags:
            updated = False
            for flag in list(st.session_state.flags.keys()):
                new_val = st.toggle(f"Flag: `{flag}`", value=st.session_state.flags[flag])
                if new_val != st.session_state.flags[flag]:
                    st.session_state.flags[flag] = new_val
                    updated = True
            if updated:
                save_flags_to_disk()
        else:
            st.info("Run refactor to populate toggles.")
    else:
        st.info("No refactored app built yet.")
