class ReasoningEngine:
    """
    SAAF reasoning layer.

    Converts user requests into
    executable plans.
    """


    def plan(self, user_request: str):

        request = user_request.lower().strip()


        # -----------------------------
        # Memory Recall
        # -----------------------------

        if "last calculation" in request:

            return {
                "action": "memory",
                "memory_key": "last_calculation"
            }


        if "what is my name" in request:

            return {
                "action": "memory",
                "memory_key": "name"
            }


        # -----------------------------
        # Memory Statement
        # -----------------------------

        if "my name is" in request:

            return {
                "action": "memory_saved",
                "memory_key": "name"
            }


        # -----------------------------
        # Tool Execution
        # -----------------------------

        if "calculate" in request:

            expression = request.replace(
                "calculate",
                ""
            ).strip()


            return {

                "action": "tool",

                "tool": "calculator",

                "input": expression
            }


        # -----------------------------
        # Unknown
        # -----------------------------

        return {

            "action": "unknown",

            "input": user_request
        }