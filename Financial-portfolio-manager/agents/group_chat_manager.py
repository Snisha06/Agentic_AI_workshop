from agents.portfolio_analysis_agent import PortfolioAnalysisAgent
from stateflow.flow_manager import FlowManager

class GroupChatManager:
    def handle_conversation(self):
        print("🤖 [Manager]: Noted. Let’s analyze your portfolio.")
        portfolio_agent = PortfolioAnalysisAgent()
        user_data = portfolio_agent.analyze_portfolio()

        flow = FlowManager()
        investment_recommendations = flow.route(user_data)

        from agents.investment_advisor_agent import InvestmentAdvisorAgent
        advisor = InvestmentAdvisorAgent()
        advisor.generate_report(user_data, investment_recommendations)
