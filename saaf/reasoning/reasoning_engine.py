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

        if "my name" in request and "is" in request:

            return {
                "action": "memory_saved",
                "memory_key": "name"
            }

        if "i know" in request:

            return {
                "action": "memory_saved",
                "memory_key": "skills"
            }
        # -----------------------------
        # Tool Execution
        # -----------------------------

        if "calculate" in request:


            expression = request.replace(
                "calculate",
                ""
            )


            # Multi-step workflow

            if "save" in expression:


                expression = (
                    expression
                    .split("and")[0]
                    .strip()
                )


                return {

                    "action":"workflow",

                    "steps":[

                        {
                            "action":"tool",

                            "tool":"calculator",

                            "input":expression

                        },

                        {
                            "action":"save_memory",

                            "memory_key":
                            "last_calculation"

                        }

                    ]

                }



            # Normal calculation

            return {

                "action":"tool",

                "tool":"calculator",

                "input":
                expression.strip()

            }

        # -----------------------------
        # Unknown
        # -----------------------------

        return {

            "action": "unknown",

            "input": user_request
        }