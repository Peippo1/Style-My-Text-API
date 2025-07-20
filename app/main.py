from fastapi import FastAPI, Form

app = FastAPI()

def apply_style(text: str, style: str) -> str:
    if style == "pirate":
        return text.replace("my", "me").replace("you", "ye").replace(".", " arrr!").capitalize()
    elif style == "sarcastic":
        return ''.join(
            c.upper() if i % 2 else c.lower()
            for i, c in enumerate(text)
        )
    elif style == "shakespeare":
        return text.replace("you", "thou").replace("are", "art").replace("do", "dost").replace("have", "hast")
    elif style == "emoji":
        return text.replace("love", "❤️").replace("happy", "😊").replace("fire", "🔥").replace("cool", "😎")
    elif style == "reverse":
        return text[::-1]
    elif style == "shouty":
        return text.upper()
    else:
        return text

@app.post("/style")
async def style_text(text: str = Form(...), style: str = Form(...)):
    styled = apply_style(text, style)
    return {"styled_text": styled}
