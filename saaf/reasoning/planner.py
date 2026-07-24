from saaf.models.intent import AgentIntent, AgentStep


class Planner:
    """
    Converts validated AgentIntent
    into executable workflow.
    """


    def create_plan(
        self,
        intent: AgentIntent
    ):

        action = intent.action


        # =================================
        # Single Tool Execution
        # =================================

        if action == "tool":

            return [

                {
                    "step": 1,

                    "action":
                    "execute_tool",

                    "tool":
                    intent.tool,

                    "input":
                    intent.input
                }

            ]


        # =================================
        # Memory Recall
        # =================================

        elif action == "memory":

            return [

                {
                    "step": 1,

                    "action":
                    "search_memory",

                    "memory_key":
                    intent.memory_key
                }

            ]


        # =================================
        # Save Memory
        # =================================

        elif action == "memory_saved":

            return [

                {
                    "step": 1,

                    "action":
                    "save_memory",

                    "memory_key":
                    intent.memory_key
                }

            ]


        # =================================
        # Multi-Step Workflow
        # =================================

        elif action == "workflow":

            execution_plan = []


            for index, step in enumerate(
                intent.steps,
                start=1
            ):


                # -------------------------
                # Tool Step
                # -------------------------

                if step.action == "tool":

                    execution_plan.append(

                        {

                            "step":
                            index,

                            "action":
                            "execute_tool",

                            "tool":
                            step.tool,

                            "input":
                            step.input

                        }

                    )


                # -------------------------
                # Memory Step
                # -------------------------

                elif step.action == "save_memory":

                    execution_plan.append(

                        {

                            "step":
                            index,

                            "action":
                            "save_memory",

                            "memory_key":
                            step.memory_key

                        }

                    )


            return execution_plan



        # =================================
        # Unknown Intent
        # =================================

        else:

            return [

                {

                    "step":1,

                    "action":
                    "unknown"

                }

            ]