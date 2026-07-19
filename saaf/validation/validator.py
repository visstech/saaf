from saaf.models.intent import (
    AgentIntent,
    AgentStep
)



class IntentValidator:
    """
    Validates LLM generated intents.
    """


    ALLOWED_ACTIONS = [

        "tool",

        "workflow",

        "memory",

        "memory_saved",

        "unknown"

    ]



    def validate(
        self,
        data: dict
    ):

        if not data:

            return AgentIntent(
                action="unknown"
            )



        action = data.get(
            "action"
        )



        if action not in self.ALLOWED_ACTIONS:

            return AgentIntent(
                action="unknown",
                raw=data
            )



        # Workflow

        if action == "workflow":


            steps=[]


            for step in data.get(
                "steps",
                []
            ):

                steps.append(

                    AgentStep(

                        action=
                        step.get(
                            "action"
                        ),

                        tool=
                        step.get(
                            "tool"
                        ),

                        input=
                        step.get(
                            "input"
                        ),

                        memory_key=
                        step.get(
                            "memory_key"
                        )

                    )

                )


            return AgentIntent(

                action="workflow",

                steps=steps,

                raw=data

            )



        # Normal action

        return AgentIntent(

            action=action,

            tool=data.get(
                "tool"
            ),

            input=data.get(
                "input"
            ),

            memory_key=data.get(
                "memory_key"
            ),

            raw=data

        )