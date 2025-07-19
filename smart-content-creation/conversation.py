from agents.content_creator import ContentCreatorAgent
from agents.content_critic import ContentCriticAgent

def run_conversation():
    creator = ContentCreatorAgent()
    critic = ContentCriticAgent()

    conversation_log = []

    # Turn 1 - Initial Draft
    draft_1 = creator.draft_content()
    review_1 = critic.review_content(draft_1)

    # Turn 2 - Revision
    draft_2 = creator.draft_content(revision_note=review_1)
    review_2 = critic.review_content(draft_2)

    # Final Output
    return draft_2, conversation_log
