import streamlit as st
from app_core import App

st.set_page_config(page_title="F5 Troubleshooter", page_icon="🖥️")
st.title("🖥️ F5 Troubleshooter - Basic Mode")

user_input = st.text_area("Describe the network issue:", height=150)

app = App(config_file='config.json', use_ollama=False)

model_name = st.selectbox("Select Analysis Scenario", app.model_selector.available_models)

if st.button("Run Analysis"):
    if not user_input.strip():
        st.warning("Please enter a network issue description.")
    else:
        with st.spinner("Analyzing..."):
            result = app.run(user_input, model_name)

        st.subheader("📝 Result")
        st.text(result["ai_output"])
