import time
import json
import requests

def save(data):
    with open("dataset.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")

def scrape_kahoot(kahoot_id):
    url = f"https://kahoot.it/rest/kahoots/{kahoot_id}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    time.sleep(1)

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return None

    data = r.json()
    save(data)
    return data

def search_kahoots(query):
    url = f"https://create.kahoot.it/rest/kahoots/?query={query}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return []

    data = r.json()
    ids = [k["uuid"] for k in data.get("entities", [])]
    return ids

def scrape_from_search(query):
    ids = search_kahoots(query)
    results = []

    for kid in ids:
        data = scrape_kahoot(kid)
        if data:
            results.append(kid)

    return results
