from crewai import Agent

# Agent that acts as user proxy (uploads images / initiates conversation)
user_proxy_agent = Agent(
    role="User Proxy Agent",
    goal="Share the bill image with the group manager to initiate processing.",
    backstory="I represent the user and know what expenses to process.",
    allow_delegation=False
)

# Agent that performs image extraction and categorization
bill_processing_agent = Agent(
    role="Bill Processing Agent",
    goal="Extract and categorize expenses from bill images.",
    backstory="I specialize in parsing images and organizing expenses into categories.",
    allow_delegation=False
)

# Agent that summarizes categorized expenses and detects trends
expense_summary_agent = Agent(
    role="Expense Summarization Agent",
    goal="Analyse categorized expenses and generate spending insights.",
    backstory="I analyze spending data to provide breakdowns and trends.",
    allow_delegation=False
)
