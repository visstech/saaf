from saaf.models.execution import ExecutionContext



class Executor:
    """
    Executes multi-step plans.
    """


    def __init__(
        self,
        tools=None,
        memory=None
    ):

        self.tools = tools

        self.memory = memory



    def execute(
        self,
        plan,
        context=None
    ):


        if context is None:

            context = ExecutionContext(

                user_id="default",

                request=""

            )



        for step in plan:


            action = step.get(
                "action"
            )


            print(
                f"[Executor] Step {step['step']} : {action}"
            )



            # --------------------
            # Tool Execution
            # --------------------

            if action == "execute_tool":


                result = (
                    self.tools.execute_plan(
                        {
                            "tool":
                            step["tool"],

                            "input":
                            step["input"]
                        }
                    )
                )


                context.add_result(
                    result
                )


                if isinstance(result, dict):

                    if "output" in result:

                        context.set_variable(

                            "last_result",

                            result["output"]

                        )



            # --------------------
            # Memory Search
            # --------------------

            elif action == "search_memory":


                result = self.memory.recall(

                    context.user_id,

                    step["memory_key"]

                )


                context.add_result(
                    result
                )



            # --------------------
            # Save Memory
            # --------------------

            elif action == "save_memory":


                value = context.get_variable(

                    "last_result"

                )


                context.add_result(

                    {
                        "saved":
                        value
                    }

                )



        return context