class ContentCriticAgent:
    def __init__(self):
        self.role = "Content Critic Agent"

    def review_content(self, content: str):
        if "What is Generative AI?" in content:
            return (
                "The content is a good start but could be improved by:\n"
                "- Adding technical details like training methods or examples of specific models.\n"
                "- Avoiding repetition and using clearer headings.\n"
                "- Making the language more structured and refined."
            )
        else:
            return (
                "Much improved! The revised content adds clarity, specific model examples, and practical applications.\n"
                "Final suggestion: consider mentioning ethical concerns or limitations briefly for a well-rounded view."
            )
