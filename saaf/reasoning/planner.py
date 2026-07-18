class Planner:
    """
    Converts intent into
    executable workflow.
    """


    def create_plan(
        self,
        intent
    ):


        action = intent.get(
            "action"
        )


        # ---------------------
        # Tool workflow
        # ---------------------

        if action == "tool":

            return [

                {
                    "step":1,

                    "action":
                    "execute_tool",

                    "tool":
                    intent["tool"],

                    "input":
                    intent["input"]

                }

            ]



        # ---------------------
        # Memory search
        # ---------------------

        elif action == "memory":

            return [

                {
                    "step":1,

                    "action":
                    "search_memory",

                    "memory_key":
                    intent["memory_key"]

                }

            ]



        # ---------------------
        # Save memory workflow
        # ---------------------

        elif action == "memory_saved":

            return [

                {
                    "step":1,

                    "action":
                    "save_memory",

                    "memory_key":
                    intent["memory_key"]

                }

            ]
            
        elif action == "workflow":

            execution_plan=[]


            for index, step in enumerate(
                intent["steps"],
                start=1
            ):

                if step["action"]=="tool":

                    execution_plan.append({

                        "step":index,

                        "action":
                        "execute_tool",

                        "tool":
                        step["tool"],

                        "input":
                        step["input"]

                    })


        elif step["action"]=="save_memory":

            execution_plan.append({

                "step":index,

                "action":
                "save_memory",

                "memory_key":
                step["memory_key"]

            })


        return execution_plan