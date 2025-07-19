from agents.query_router import route_query
from agents.competitor_search import search_competitors
from agents.report_generator import generate_report

def main():
    print("Welcome to the Retail Competitor Conversational AI!")
    user_query = input("Ask your question about local clothing competitors: ")

    route = route_query(user_query)

    if route == "search":
        competitors = search_competitors(user_query)
        report = generate_report(user_query, competitors)
        print("\n--- Competitor Report ---\n")
        print(report)
    else:
        print("Sorry, this assistant currently only handles competitor search queries.")

if __name__ == "__main__":
    main()
