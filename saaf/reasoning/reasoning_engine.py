class ReasoningEngine:

    def think(self, user_request: str):

        user_request = user_request.lower()

        if "calculate" in user_request:

            expression = user_request.replace(
                "calculate",
                ""
            ).strip()

            return {
                "tool": "calculator",
                "input": expression
            }

        return None