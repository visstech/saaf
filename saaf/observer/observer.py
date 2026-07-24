class Observer:


    def analyze(self, result):

        if isinstance(result, dict):

            status = result.get(
                "status"
            )


            if status == "SUCCESS":

                return {
                    "action": "CONTINUE",
                    "message": "Tool executed successfully"
                }


            elif status == "FAILED":

                return {
                    "action": "RETRY",
                    "message": result.get(
                        "message"
                    )
                }


        return {
            "action": "CONTINUE",
            "message": "Result received"
        }