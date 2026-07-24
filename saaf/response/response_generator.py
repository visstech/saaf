class ResponseGenerator:
    """
    Generates final human-readable responses.

    Uses FormatterRegistry to dynamically
    select the correct formatter.
    """


    def __init__(
        self,
        formatter_registry
    ):

        self.formatter_registry = formatter_registry



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


        # WorkflowState support

        if hasattr(
            result,
            "results"
        ):

            result = result.results



        # Workflow result list

        if isinstance(
            result,
            list
        ):


            responses = []


            for item in result:


                if not isinstance(
                    item,
                    dict
                ):

                    continue


                response = (
                    self.formatter_registry.format(
                        item
                    )
                )


                if response:

                    responses.append(
                        response
                    )


            if responses:

                return " ".join(
                    responses
                )



        # Single tool result

        if isinstance(
            result,
            dict
        ):


            response = (
                self.formatter_registry.format(
                    result
                )
            )


            if response:

                return response



            if "message" in result:

                return result["message"]



        return (
            "I could not understand."
        )