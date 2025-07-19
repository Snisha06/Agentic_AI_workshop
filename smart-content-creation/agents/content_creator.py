class ContentCreatorAgent:
    def __init__(self):
        self.role = "Content Creator Agent"

    def draft_content(self, revision_note=""):
        if not revision_note:
            return (
                "## What is Generative AI?\n"
                "Generative AI refers to artificial intelligence models capable of generating new data such as text, images, music, or code. "
                "These models learn from large datasets and generate outputs based on learned patterns. Examples include GPT-4, DALL·E, and Stable Diffusion.\n"
                "\n"
                "Generative AI is widely used in industries like content creation, customer support, game development, and healthcare."
            )
        else:
            return (
                "## Understanding Generative AI\n"
                "Generative AI is a field within artificial intelligence that focuses on creating systems capable of generating new content. "
                "These systems are trained on massive datasets and use learned patterns to produce outputs like text, images, audio, or video. "
                "\n\nExamples of generative AI models include OpenAI's GPT-4 (for text), DALL·E (for images), and Google’s MusicLM (for audio). "
                "\n\nIts applications range from creative writing and design to medical imaging and drug discovery."
            )
