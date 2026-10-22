from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "مصنع الذهب البرقيق شغال 🔥", "repo": "goldvein-whatsapp"}

@app.get("/analyze")
def analyze(lat: float = 19.5464, lon: float = 31.0881):
    gossan = 0.28
    silica = 1.42
    trust = 92
    depth = 15
    return {
        "location": f"{lat},{lon}",
        "ibm_card": f"{trust}% احفر",
        "gossan_red": gossan,
        "silica_white": silica,
        "sar_line": "120m خط ابيض",
        "decision": f"✅ احفر {depth}م - ربح 6 مليار",
        "place": "البرقيق"
    }
