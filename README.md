# 🔭 AstroBot — Deep Space AI Agent

<div align="center">

![AstroBot Banner](https://images-assets.nasa.gov/image/PIA12348/PIA12348~thumb.jpg)

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3-orange?style=for-the-badge&logo=groq&logoColor=white)](https://console.groq.com)
[![NASA API](https://img.shields.io/badge/NASA-API-red?style=for-the-badge&logo=nasa&logoColor=white)](https://api.nasa.gov)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**An intelligent astronomy AI agent that answers deep space questions with structured scientific responses, real NASA images, and trending research — completely free.**

[🚀 Live Demo](#) · [📖 Documentation](#how-it-works) · [🐛 Report Bug](../../issues) · [✨ Request Feature](../../issues)

</div>

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Roadmap](#roadmap)
- [Author](#author)

---

## 🌌 About the Project

AstroBot is a full-stack AI agent web application built for astronomy enthusiasts, students, and researchers. Ask any question about the universe — from black holes to the Big Bang — and AstroBot responds with structured scientific answers, real NASA space imagery, and the latest research trends.

This project was built as **Day 1 of a 120-day AI/ML engineering transformation** — starting from zero and building toward production-grade AI systems.

> *"The cosmos is within us. We are made of star-stuff."* — Carl Sagan

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **AI Agent** | Powered by Groq + LLaMA 3.3 70B — structured responses with derivations |
| 🖼️ **NASA Images** | Real space photos fetched live from NASA Image Library |
| 🌠 **APOD** | NASA Astronomy Picture of the Day in sidebar |
| 📰 **Trending Research** | Latest 2023-2025 astronomy discoveries and missions |
| 💬 **Chat Memory** | Full conversation history within each session |
| 🆓 **100% Free** | No paid APIs required — Groq free tier + NASA free APIs |
| 📱 **Responsive** | Works on desktop and mobile browsers |

---

## 🛠️ Tech Stack

**Backend**
- Python 3.10+
- Flask 3.0
- Groq SDK (LLaMA 3.3 70B Versatile)

**Frontend**
- HTML5 / CSS3 / Vanilla JavaScript
- Marked.js (Markdown rendering)
- Custom space-themed UI

**APIs (All Free)**
- [Groq API](https://console.groq.com) — AI responses via LLaMA 3.3 70B
- [NASA Image and Video Library](https://images.nasa.gov) — Space images
- [NASA APOD API](https://api.nasa.gov) — Picture of the Day

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- A free Groq API key from [console.groq.com](https://console.groq.com)

### Step 1 — Clone the Repository

```bash
git clone https://github.com/tanmayakumar9070-ctrl/astrobot.git
cd astrobot
```

### Step 2 — Get Your Free Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign in / Sign up
3. Click **API Keys** → **Create API Key**
4. Copy the key

### Step 3 — Add Your API Key

Create a file called `config.py` in the project folder:

```python
GROQ_API_KEY = "paste_your_groq_key_here"
```

> ⚠️ `config.py` is in `.gitignore` — it will never be pushed to GitHub.

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5 — Run the Application

```bash
python Astrobot.py
```

### Step 6 — Open in Browser

```
http://localhost:5000
```

🎉 **AstroBot is live!**

---

## 📁 Project Structure

```
astrobot/
│
├── Astrobot.py             # Flask backend — API routes, AI agent logic
├── requirements.txt        # Python dependencies
├── config.py               # 🔒 Your API key (NOT pushed to GitHub)
├── .gitignore              # Protects secrets from being committed
├── README.md               # You are here
│
└── templates/
    └── index.html          # Frontend — UI, chat interface, styling
```

---

## ⚙️ How It Works

```
User Question
      │
      ▼
Flask Backend (Astrobot.py)
      │
      ├──► Groq API (LLaMA 3.3 70B)
      │         │
      │         ▼
      │    Structured Response
      │    (Answer + Derivation +
      │     Implications + Insights)
      │
      └──► NASA Image Library API
                │
                ▼
           Relevant Space Images
                │
                ▼
         Combined Response
         sent to Frontend
```

### Response Structure

Every AstroBot answer follows this format:

```
🔭 CORE ANSWER         — Scientific answer with real data
📐 MATHEMATICAL DERIVATION — Physics, equations, step by step
🌌 LATEST DISCOVERIES  — JWST, EHT, LIGO, Gaia findings 2023-2025
🧠 DEEP IMPLICATIONS   — Philosophy, humanity, unsolved paradoxes
💡 KEY INSIGHTS        — 5 surprising facts
🔗 EXPLORE FURTHER     — Papers and missions to investigate
```

---

## 🗺️ Roadmap

- [x] Groq + LLaMA 3.3 AI agent
- [x] NASA image integration
- [x] Structured scientific responses
- [x] APOD sidebar
- [x] Conversation memory
- [ ] AstroBot v2 — RAG system with astronomy knowledge base
- [ ] Web search integration for real-time discoveries
- [ ] Agentic reasoning — multi-step space research
- [ ] Voice input support
- [ ] Mobile app (Android APK)

---

## 📊 Project Status

```
Day 1 of 120 — Foundation Phase
Status: Active Development
Next: Add RAG pipeline (Day 65-80)
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License.

---

## 👨‍💻 Author

**Tanmaya Kumar Sahoo**

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/tanmayakumar9070-ctrl)

> Built as part of a 120-day AI/ML Engineering transformation — from zero to production-grade AI systems.

---

<div align="center">

**⭐ Star this repo if you found it useful!**

Made with ❤️ and curiosity about the cosmos

</div>
