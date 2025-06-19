# utils/data_loader.py
# ----------------------------
import json

def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
