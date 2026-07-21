from saaf.models.intent import (
    AgentIntent,
    AgentStep
)


class IntentValidator:
    """
    Validates and normalizes LLM generated intents.

    Converts raw LLM JSON output into
    strongly typed AgentIntent objects.
    """


    ALLOWED_ACTIONS = [

        "tool",

        "workflow",

        "memory",

        "save_memory",

        "memory_saved",

        "unknown"

    ]


    ACTION_NORMALIZATION = {

        "memory_saved": "save_memory",

        "remember": "save_memory",

        "store_memory": "save_memory"

    }



    def validate(
        self,
        data: dict
    ):
        """
        Validate raw LLM JSON intent.

        Returns:
            AgentIntent
        """


        if not data:

            return AgentIntent(
                action="unknown"
            )



        action = data.get(
            "action"
        )



        # ==================================
        # Normalize action names
        # ==================================

        action = self.ACTION_NORMALIZATION.get(
            action,
            action
        )



        # ==================================
        # Validate action
        # ==================================

        if action not in self.ALLOWED_ACTIONS:

            return AgentIntent(

                action="unknown",

                raw=data

            )



        # ==================================
        # Workflow Intent
        # ==================================

        if action == "workflow":


            steps = []


            for step in data.get(
                "steps",
                []
            ):


                step_action = step.get(
                    "action"
                )


                # Normalize workflow step action

                step_action = self.ACTION_NORMALIZATION.get(

                    step_action,

                    step_action

                )



                steps.append(

                    AgentStep(

                        action=step_action,

                        tool=step.get(
                            "tool"
                        ),

                        input=step.get(
                            "input"
                        ),

                        memory_key=step.get(
                            "memory_key"
                        )

                    )

                )



            return AgentIntent(

                action="workflow",

                steps=steps,

                raw=data

            )



        # ==================================
        # Single Action Intent
        # ==================================

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