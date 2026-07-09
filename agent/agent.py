from tools.tool_manager import ToolManager


class AIAgent:

    def __init__(self):

        self.tool_manager = ToolManager()

    def process_request(self, user_request: str):

        print("User Request:")
        print(user_request)