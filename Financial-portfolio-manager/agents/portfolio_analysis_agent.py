class PortfolioAnalysisAgent:
    def analyze_portfolio(self):
        print("\n📊 Portfolio Analysis Started...\n")
        salary = float(input("Enter your monthly salary: ₹"))
        fixed_deposits = float(input("Amount in Fixed Deposits: ₹"))
        sips = float(input("Amount in SIPs: ₹"))
        real_estate = float(input("Value in Real Estate: ₹"))

        total_assets = fixed_deposits + sips + real_estate
        category = "Growth" if sips < salary * 1.5 else "Value"

        print(f"\n📈 Investment Category Identified: {category}\n")
        return {
            "salary": salary,
            "fixed_deposits": fixed_deposits,
            "sips": sips,
            "real_estate": real_estate,
            "category": category
        }
