import streamlit as st
import requests

# Function (Hybrid: AI + Fallback)
def analyze_log(log, issue_type):

    prompt = f"""
    You are a senior F5 L3 network engineer.

    Analyze the issue below:

    {log}

    Provide:
    1. Root Cause
    2. Troubleshooting steps
    3. Fix
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=5
        )

        return response.json()["response"]

    except:
        # Fallback logic with command suggestion
        if "VIP" in log or issue_type == "VIP Down":
            return {
                "analysis": """Root Cause:
All pool members down or VIP disabled

Troubleshooting:
1. Check virtual server status
2. Verify pool members
3. Check health monitor

Fix:
Enable VIP or fix backend servers
""",
                "command": "tmsh show ltm pool"
            }

        elif "SSL" in log or issue_type == "SSL Issue":
            return {
                "analysis": """Root Cause:
SSL certificate issue

Troubleshooting:
1. Check SSL profile
2. Verify certificate expiry
3. Check cipher settings

Fix:
Update certificate
""",
                "command": "tmsh list ltm profile client-ssl"
            }

        elif "timeout" in log or issue_type == "Timeout":
            return {
                "analysis": """Root Cause:
Backend server not responding

Troubleshooting:
1. Check pool members
2. Ping backend servers
3. Check firewall rules

Fix:
Restart backend or fix network issue
""",
                "command": "tmsh show ltm pool"
            }

        else:
            return "⚠️ Ollama not ready. Showing basic analysis."


# UI Config
st.set_page_config(page_title="F5 Troubleshooter", layout="centered")

st.title("🔧 F5 AI Troubleshooter (Hybrid AI + Automation)")

st.info("Supports AI + Command Suggestion + Automation Simulation")

# Dropdown
issue_type = st.selectbox(
    "Select Issue Type",
    ["General", "VIP Down", "SSL Issue", "Timeout"]
)

# File Upload
uploaded_file = st.file_uploader("Upload log file (.txt)")

# Input Handling
if uploaded_file is not None:
    log = uploaded_file.read().decode("utf-8")
else:
    log = st.text_area("Enter your log or issue:")

# Button
if st.button("Analyze"):

    if not log:
        st.warning("Please enter or upload a log")
    else:
        with st.spinner("Analyzing issue..."):
            result = analyze_log(log, issue_type)

        st.subheader("🤖 Analysis Result")

        if isinstance(result, dict):
            st.write(result["analysis"])

            st.subheader("💻 Suggested Command")
            st.code(result["command"])

            if st.button("Run Fix (Simulation)"):
                st.success("Executing command...")
                st.write("Output: Pool members are DOWN")

        else:
            st.write(result)
