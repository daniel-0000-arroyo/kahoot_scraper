import time
import json
import requests

def scrape_kahoot(kahoot_id):
    url = f"https://kahoot.it/rest/kahoots/{kahoot_id}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    time.sleep(5)

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return None

    data = r.json()

    with open("dataset.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")

    return data
