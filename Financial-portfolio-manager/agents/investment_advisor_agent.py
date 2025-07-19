class InvestmentAdvisorAgent:
    def generate_report(self, data, recommendations):
        print("\n📄 Final Personalized Investment Report")
        print("----------------------------------------")
        print(f"💰 Salary: ₹{data['salary']}")
        print("📂 Portfolio:")
        print(f"  - Fixed Deposits: ₹{data['fixed_deposits']}")
        print(f"  - SIPs: ₹{data['sips']}")
        print(f"  - Real Estate: ₹{data['real_estate']}")
        print(f"\n📌 Category: {data['category']}")
        print("\n💡 Recommended Investments:")
        for r in recommendations:
            print(f"  - {r}")
        print("\n📘 Advice: Diversify regularly and rebalance your assets every 6 months.\n")
