from fastapi import FastAPI, Form, Request, Depends
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

app = FastAPI()

# Create a limiter instance using IP address for client identity
limiter = Limiter(key_func=get_remote_address)

# Register the handler for rate limit errors
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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
@limiter.limit("5/minute")
async def style_text(
    request: Request,
    text: str = Form(...),
    style: str = Form(...)
):
    styled = apply_style(text, style)
    return {"styled_text": styled}
