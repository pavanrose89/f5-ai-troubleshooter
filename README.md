# 🔧 F5 AI Troubleshooter

> AI-powered troubleshooting assistant for F5 / Network Engineers  
> Built with Python, Streamlit, and Local LLM (Ollama)

---

## 🚀 Overview

F5 AI Troubleshooter is a smart tool that helps engineers quickly diagnose network issues such as **VIP down, SSL errors, and timeouts**.

It provides:
- Root cause analysis
- Step-by-step troubleshooting
- Suggested F5 commands
- Automation simulation

---

## ✨ Features

- 🔍 Analyze real-world network issues
- 🤖 AI-powered insights (via Ollama)
- ⚡ Works even without AI (fallback logic)
- 📂 Upload log files (.txt)
- 💻 Suggested F5 commands
- 🛠 Simulated automation (Run Fix)
- 🎨 Clean and interactive UI

---

## 🧠 How It Works
User Input (UI)
↓
Analysis Engine (AI + Rules)
↓
Decision Logic
↓
Output (Root Cause + Fix + Commands)

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Ollama (Local LLM)  
- Requests  

---

## ▶️ Getting Started

### 1️⃣ Install dependencies

```bash
pip install streamlit requests

2️⃣ Start AI model (optional)

ollama run llama3

3️⃣ Run application

streamlit run UI.py

🧪 Example Inputs

VIP Issue

VIP down and application not accessible


SSL Issue

SSL handshake failure on VIP


Timeout Issue

Connection timeout from client

## 📸 Screenshots

![UI](https://raw.githubusercontent.com/pavanrose89/f5-ai-troubleshooter/main/images/UI.png)

![Result](https://raw.githubusercontent.com/pavanrose89/f5-ai-troubleshooter/main/images/Result.png)


⭐ Support

If you found this useful, consider giving a ⭐ on GitHub!
