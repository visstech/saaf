from datetime import datetime


class ConversationMemory:

    def __init__(self):
        self.messages = []


    def add_message(self, role, content):

        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now()
        }

        self.messages.append(message)


    def get_history(self):

        return self.messages.copy()


    def clear(self):

        self.messages.clear()
    
    