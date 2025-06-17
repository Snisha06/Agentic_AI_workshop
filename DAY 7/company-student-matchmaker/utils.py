import json
import streamlit as st

def load_data(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Failed to load {path}: {str(e)}")
        return []
