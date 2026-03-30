# 🔧 F5 AI Troubleshooter

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![AI](https://img.shields.io/badge/AI-Enabled-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Made With Love](https://img.shields.io/badge/Made%20with-❤️-red)


> AI-powered troubleshooting assistant for F5 / Network Engineers
> Built using Python, Streamlit, and hybrid logic (AI + fallback)

---

## 🚀 Overview

F5 AI Troubleshooter is a smart tool designed to help engineers quickly diagnose and resolve network issues such as:

* VIP down
* SSL handshake failures
* Application timeouts

It combines **AI-based analysis** with **rule-based fallback logic** to ensure reliable results in all scenarios.

---

## 🔥 Highlights

* Built real-world F5 troubleshooting assistant
* Hybrid architecture (AI + fallback logic)
* Works even when AI is unavailable
* Clean UI built with Streamlit
* Command suggestion + automation simulation

---

## 🎥 Demo

![Demo](images/demo.gif)

---

## ✨ Features

* 🤖 AI-powered analysis (when available)
* ⚡ Basic fallback logic (always works)
* 📂 Upload log files (.txt)
* 💻 Suggested F5 commands
* 🛠 Automation simulation (Run Fix)
* 🎨 Simple and interactive UI

---

## 🧠 How It Works

```
User Input (UI)
      ↓
Analysis Engine (AI + Rules)
      ↓
Decision Logic
      ↓
Output (Root Cause + Fix + Commands)
```

---

## 🤖 AI Integration

* Uses local LLM (Ollama) or API-based AI
* Sends structured prompts for analysis
* Returns root cause, troubleshooting steps, and fixes
* Falls back to rule-based logic if AI is unavailable

---

## 📁 Project Structure

```
UI.py             # Hybrid version (Basic + AI)
ui-olam.py        # Ollama-only AI version
requirements.txt
README.md
images/           # Screenshots / demo
```

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Ollama (optional local AI)
* Requests

---

## ▶️ Getting Started

### 1️⃣ Install dependencies

```bash
pip install streamlit requests
```

---

### 2️⃣ (Optional) Start AI

```bash
ollama run phi3
```

---

### 3️⃣ Run application

```bash
streamlit run UI.py
```

---

## 🧪 Example Inputs

```
VIP down and application not accessible
```

```
SSL handshake failure on VIP
```

```
Connection timeout from client
```

---

## 💼 Use Case

This tool helps:

* Network Engineers
* F5 Administrators
* Support Engineers

Quickly troubleshoot production issues with minimal effort.

---

## 🔮 Future Enhancements

* 🔗 Real F5 device integration (SSH / API)
* 💬 Chat-based interface
* 📊 Dashboard & analytics
* ☁️ Cloud deployment

---

## 🙌 Key Learnings

* AI + Networking integration
* Prompt engineering
* UI development with Streamlit
* Hybrid system design (AI + fallback)

---

## ⭐ Support

If you found this useful, consider giving a ⭐ on GitHub!
