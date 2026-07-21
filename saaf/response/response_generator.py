from saaf.models.memory import Memory


class ResponseGenerator:
    """
    Converts agent execution results
    into human-readable responses.

    Supports:
    - Tool results
    - Workflow results
    - Memory responses
    - Message responses
    """


    def generate(
        self,
        result
    ):

        print("[DEBUG RESPONSE INPUT]")
        print(type(result))
        print(result)


        if result is None:

            return (
                "I could not process the request."
            )


        calculator_result = None
        memory_saved = False


        # ==========================================
        # WorkflowState Support
        # ==========================================

        if hasattr(
            result,
            "results"
        ):

            result = result.results



        # ==========================================
        # Workflow Result List Support
        # ==========================================

        if isinstance(
            result,
            list
        ):


            for item in result:


                if not isinstance(
                    item,
                    dict
                ):

                    continue



                # Calculator result

                if (

                    item.get("tool")
                    == "calculator"

                    and "output"
                    in item

                ):

                    calculator_result = item



                # Memory saved

                if item.get(
                    "memory_saved"
                ):

                    memory_saved = True



            response = ""



            if calculator_result:

                value = calculator_result["output"]

                if isinstance(value, float):
                    value = round(value, 4)

                response = (
                    f"The result of "
                    f"{calculator_result['input']} "
                    f"is {value}."
                )



            if memory_saved:


                response += (

                    " I have saved this result "
                    "in memory."

                )



            if response:

                return response



        # ==========================================
        # Single Calculator Dictionary
        # ==========================================

        if isinstance(
            result,
            dict
        ):


            if (

                result.get("tool")
                == "calculator"

                and "output"
                in result

            ):


                return (

                    f"The result of "
                    f"{result['input']} "
                    f"is "
                    f"{result['output']}."

                )



        # ==========================================
        # Memory Object Response
        # ==========================================

        if isinstance(
            result,
            Memory
        ):


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
                    f"= "
                    f"{value['result']}."

                )



        # ==========================================
        # Message Dictionary
        # ==========================================

        if isinstance(
            result,
            dict
        ):


            if "message" in result:

                return result["message"]



        return (
            "I could not understand."
        )