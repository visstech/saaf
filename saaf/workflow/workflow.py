class WorkflowEngine:
    """
    Executes workflow steps.
    """




    def __init__(self, registry):

        self.registry = registry



    def run(self, plan, state):

            state.status = "running"

            for step in plan:

                action = step["action"]

                node = self.registry.get(action)

                if node is None:

                    raise ValueError(

                        f"No workflow node registered for '{action}'"

                    )

                print(
                    f"[Workflow] Running {action}"
                )

                state = node.execute(
                    state,
                    step
                )

            state.status = "completed"

            return state