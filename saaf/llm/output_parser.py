import json
import re


class LLMOutputParser:
    """
    Converts LLM responses into
    structured SAAF intents.
    """


    def parse(
        self,
        response: str
    ):

        if not response:

            return {
                "action":"unknown"
            }


        response = response.strip()


        # -----------------------------
        # Remove markdown JSON blocks
        # -----------------------------

        response = (
            response
            .replace(
                "```json",
                ""
            )
            .replace(
                "```",
                ""
            )
            .strip()
        )


        # -----------------------------
        # Extract JSON
        # -----------------------------

        try:

            return json.loads(
                response
            )


        except Exception:


            match = re.search(
                r"\{.*\}",
                response,
                re.DOTALL
            )


            if match:

                try:

                    return json.loads(
                        match.group()
                    )

                except Exception:

                    pass



        return {

            "action":"unknown",

            "raw":response

        }