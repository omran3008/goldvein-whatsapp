from fastapi import FastAPI, Request, Query
from fastapi.responses import PlainTextResponse

app = FastAPI()

VERIFY_TOKEN = "gold_bariq_123"

@app.get("/")
def home():
    return {"status": "مصنع الذهب البريق شغال"}

@app.get("/webhook")
def verify_webhook(mode: str = Query(None, alias="hub.mode"), token: str = Query(None, alias="hub.verify_token"), challenge: str = Query(None, alias="hub.challenge")):
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(content=challenge)
    return PlainTextResponse(content="Forbidden", status_code=403)

@app.post("/webhook")
async def webhook_handler(request: Request):
    data = await request.json()
    print(data)
    return {"status": "ok"}
