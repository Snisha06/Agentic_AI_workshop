# tools.py
import requests
from langchain.tools import tool
from duckduckgo_search import ddg_answers

@tool
def get_weather(city: str) -> str:
    """
    Fetch current weather for a city via WeatherAPI.com.
    Requires WEATHER_API_KEY environment variable.
    """
    import os
    key = os.getenv("WEATHER_API_KEY")
    if not key:
        return "Error: WEATHER_API_KEY not set."
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}"
    resp = requests.get(url).json()
    if resp.get("error"):
        return f"Weather API error: {resp['error']['message']}"
    cur = resp["current"]
    return (f"{city}: {cur['condition']['text']}, "
            f"{cur['temp_c']}°C, humidity {cur['humidity']}%.")

@tool
def get_attractions(city: str) -> str:
    """
    Fetch top attractions via DuckDuckGo search answers.
    """
    res = ddg_answers(city + " top tourist attractions")
    if not res:
        return "No attractions found."
    return res
