class ReasoningEngine:
    """
    SAAF Reasoning Engine.

    Converts user requests into
    executable plans.
    """

    def plan(self, user_request: str):

        request = user_request.lower()

        if "calculate" in request:

            expression = request.replace(
                "calculate",
                ""
            ).strip()

            return {
                "tool": "calculator",
                "input": expression
            }


        return {
            "tool": None,
            "input": user_request
        }