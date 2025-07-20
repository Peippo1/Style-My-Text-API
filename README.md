
# Style My Text API

# Style My Text API

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-green)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


A playful FastAPI-powered microservice that transforms input text into various fun styles like **pirate**, **sarcastic**, and more.

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
🧠 Built with FastAPI for fun and learning.