from agents.group_chat_manager import GroupChatManager

class UserProxyAgent:
    def __init__(self):
        self.manager = GroupChatManager()

    def initiate_conversation(self):
        print("👤 [User]: I’d like to manage my investments.")
        self.manager.handle_conversation()
