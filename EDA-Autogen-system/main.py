import pandas as pd
from agents.admin_agent import AdminAgent

def main():
    df = pd.read_csv("data/sample.csv")  # Edit the path to your CSV
    admin = AdminAgent()
    report, feedback, validation = admin.orchestrate(df)

    print("\n=== EDA REPORT ===\n")
    print(report[:500] + "...")  # Printing head
    print("\n=== CRITIC FEEDBACK ===\n", feedback)
    print("\n=== VALIDATION ===\n", validation)

if __name__ == "__main__":
    main()
