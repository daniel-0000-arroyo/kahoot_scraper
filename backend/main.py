from fastapi import FastAPI
from scraper import scrape_kahoot

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/scrape/{kahoot_id}")
def scrape(kahoot_id: str):
    data = scrape_kahoot(kahoot_id)
    return {"status": "ok", "kahoot_id": kahoot_id, "saved": bool(data)}
