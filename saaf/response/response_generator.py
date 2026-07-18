from saaf.models.memory import Memory


class ResponseGenerator:
    """
    Converts agent execution results
    into human-readable responses.
    """


    def generate(self, result):


        if result is None:
            return "I could not process the request."


        # -----------------------------
        # Calculator Response
        # -----------------------------

        if isinstance(result, dict):

            if (
                result.get("tool")
                == "calculator"
                and "output" in result
            ):

                return (
                    f"The result of "
                    f"{result['input']} "
                    f"is {result['output']}."
                )


        # -----------------------------
        # Memory Object Response
        # -----------------------------

        if isinstance(result, Memory):

            if result.memory_key == "name":

                return (
                    f"Your name is "
                    f"{result.memory_value}."
                )


            if result.memory_key == "last_calculation":

                value = result.memory_value

                return (
                    f"Your last calculation was "
                    f"{value['expression']} "
                    f"= {value['result']}."
                )


        # -----------------------------
        # Dictionary Message Response
        # -----------------------------

        if isinstance(result, dict):

            if "message" in result:

                return result["message"]


        return "I could not understand."