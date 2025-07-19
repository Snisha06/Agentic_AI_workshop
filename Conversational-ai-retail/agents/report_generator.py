def generate_report(query: str, competitors: list) -> str:
    if not competitors:
        return "No competitor data found."

    report = f"Query: {query}\n\nNearby Competitors:\n"
    for comp in competitors:
        report += f"- {comp['name']} at {comp['location']} | Footfall: {comp['footfall']} | Peak Hours: {comp['peak_hours']}\n"
    return report
