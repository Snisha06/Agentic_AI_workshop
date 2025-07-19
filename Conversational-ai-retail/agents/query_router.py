def route_query(query: str) -> str:
    keywords = ["nearby", "footfall", "peak hours", "competitor", "store", "busy"]
    if any(word in query.lower() for word in keywords):
        return "search"
    return "unknown"
