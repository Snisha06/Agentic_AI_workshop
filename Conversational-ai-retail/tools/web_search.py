import json

def mock_web_search(query: str) -> list:
    with open("data/mock_search_data.json", "r") as file:
        data = json.load(file)
    return data.get("results", [])
