
from crewai import Task
from agents import user_proxy_agent, bill_processing_agent, expense_summary_agent

# Step 1: user uploads image
task_user = Task(
    description="User Proxy shares the bill image link or token to Group Manager.",
    expected_output="Confirmation message that the image is shared.",
    agent=user_proxy_agent
)

# Step 2: extract and categorize
task_processing = Task(
    description="Extract text from the image and categorize expenses.",
    expected_output="Categorized expenses with totals.",
    agent=bill_processing_agent
)

# Step 3: summarize and derive insights
task_summary = Task(
    description="Summarize spending trends and highlight any unusually high spending.",
    expected_output="Spending insights by category.",
    agent=expense_summary_agent
)
