from agents.growth_investment_agent import GrowthInvestmentAgent
from agents.value_investment_agent import ValueInvestmentAgent

class FlowManager:
    def route(self, user_data):
        if user_data["category"] == "Growth":
            agent = GrowthInvestmentAgent()
        else:
            agent = ValueInvestmentAgent()
        return agent.recommend(user_data)
