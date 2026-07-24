from saaf.workflow.node import WorkflowNode


class ToolNode(WorkflowNode):

    name = "tool"


    def __init__(
        self,
        tool_manager
    ):

        self.tool_manager = tool_manager



    def execute(
        self,
        state,
        step
    ):


        result = self.tool_manager.execute_plan(
            {
                "tool": step["tool"],
                "input": step["input"]
            }
        )


        state.add_result(
            result
        )


        if isinstance(result, dict):

            if "output" in result:

                state.set(
                    "last_result",
                    result["output"]
                )


        return state