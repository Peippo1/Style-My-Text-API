# Style My Text API

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-green)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://github.com/Peippo1/Style-My-Text-API/actions/workflows/test.yml/badge.svg)](https://github.com/Peippo1/Style-My-Text-API/actions/workflows/test.yml)


A playful FastAPI-powered microservice that transforms input text into various fun styles like **pirate**, **sarcastic**, and more — complete with a Streamlit frontend, CI testing, and rate limiting.

## ✨ Features

- `POST /style` endpoint that accepts text and a chosen style
- Built with FastAPI and Uvicorn
- Extendable with new style modes (e.g., Shakespearean, emoji)
- Ready to deploy and integrate

## 🚀 Getting Started

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the API locally
```bash
uvicorn app.main:app --reload
```

### Test the endpoint
Go to: [http://localhost:8000/docs](http://localhost:8000/docs)

Example input:
- `text`: "You should see my code now."
- `style`: "pirate"

## 🛠 Example Response
```json
{
  "styled_text": "Ye should see me code now arrr!"
}
```

## 📄 License

This project is open-sourced under the MIT License. See `LICENSE` for details.

---
## ✅ Final Features

- FastAPI backend deployed on Render: [https://style-my-text-api.onrender.com](https://style-my-text-api.onrender.com)
- Streamlit frontend for user interaction
- GitHub Actions CI for automated testing
- Rate limiting using `slowapi` to prevent spam

---
🧠 Built with FastAPI and Streamlit for fun, learning, and production-ready API practice.