class Agent:
    """
    Core SAAF Agent.

    Responsible for managing the
    complete lifecycle and execution
    of an AI agent.
    """

    def __init__(
        self,
        name="SAAF-Agent",
        memory=None,
        reasoning=None,
        tools=None,
        observer=None,
    ):

        self.name = name
        self.status = "initialized"

        # Core Components
        self.memory = memory
        self.reasoning = reasoning
        self.tools = tools
        self.observer = observer


    def run(self, request):
        """
        Execute a user request
        through the SAAF pipeline.
        """

        self.status = "running"

        print(f"[Agent] Request received : {request}")


        # 1. Observer Layer
        if self.observer:
            print("[Observer] Active")


        # 2. Memory Layer
        if self.memory:
            print("[Memory] Connected")


        # 3. Reasoning Layer
        if self.reasoning:

            print("[Reasoning] Creating plan...")

            plan = self.reasoning.plan(request)

            print(f"[Reasoning] Plan : {plan}")

        else:
            plan = None



        # 4. Tool Execution Layer
        if plan and self.tools:

            print("[Tools] Executing...")

            result = self.tools.execute_plan(
                plan
            )

        else:

            result = (
                f"{self.name} received request: "
                f"{request}"
            )


        # 5. Update status

        self.status = "completed"


        return result