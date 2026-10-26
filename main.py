from fastapi import FastAPI, Request, Query
from fastapi.responses import PlainTextResponse

app = FastAPI()
VERIFY_TOKEN = "gold_bariq_123"

@app.get("/")
def home():
    return {"status": "مصنع الذهب البريق شغال 🔥"}

@app.get("/analyze")
def analyze(lat: float = 19.5464, lon: float = 31.0881):
    return {"location": f"{lat},{lon}", "ibm_card": "92% احفر", "gossan_red": 0.28, "silica_white": 1.42, "sar_line": "120m خط ابيض", "decision": "✅ احفر 15م - ربح 6 مليار", "place": "البريق"}

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
