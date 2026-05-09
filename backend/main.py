from fastapi import FastAPI
from scraper import scrape_kahoot, search_kahoots, scrape_from_search

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/scrape/{kahoot_id}")
def scrape(kahoot_id: str):
    data = scrape_kahoot(kahoot_id)
    return {"kahoot_id": kahoot_id, "saved": bool(data)}

@app.get("/search/{query}")
def search(query: str):
    ids = search_kahoots(query)
    return {"query": query, "results": ids}

@app.get("/scrape_search/{query}")
def scrape_search(query: str):
    saved = scrape_from_search(query)
    return {"query": query, "scraped": saved}
