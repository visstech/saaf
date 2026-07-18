from saaf.workflow.node import WorkflowNode


class CalculatorNode(WorkflowNode):
    """
    Workflow node responsible for executing
    calculator tool operations.
    """

    name = "execute_tool"

    def __init__(self, tools):
        self.tools = tools

    def execute(self, state, step):

        result = self.tools.execute_plan({

            "tool": step["tool"],

            "input": step["input"]

        })

        state.add_result(result)

        if isinstance(result, dict):

            if "output" in result:

                state.set(

                    "last_result",

                    result["output"]

                )

        return state