from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/check/{nick}")
def check_nick(nick: str):
    try:
        with open("allowed.json", "r") as f:
            allowed = json.load(f)["allowed"]
    except:
        allowed = []

    if nick in allowed:
        return {"status": "granted"}
    else:
        return {"status": "denied"}
