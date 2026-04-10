import streamlit as st
import requests

st.set_page_config(page_title="Legal First Aid", page_icon="⚖️")

st.title("⚖️ Legal First Aid")
st.caption("Empowering you with 2026 BNS Legal Rights & Procedures")

# 1. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Chat Input
if prompt := st.chat_input("How can I help you with your legal rights today?"):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 4. Call n8n Webhook
    with st.chat_message("assistant"):
        with st.status("Searching Legal SOPs...", expanded=True):
            try:
                # Replace with your ACTUAL n8n Webhook URL
                N8N_WEBHOOK_URL = st.secrets["N8N_URL"]
                response = requests.post(N8N_WEBHOOK_URL, json={"query": prompt})
                response.raise_for_status()

                # Assume n8n returns {"output": "The legal answer..."}
                full_response = response.json().get("output", "I'm sorry, I couldn't process that.")

            except Exception as e:
                full_response = f"Connection Error: {str(e)}"

        st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})