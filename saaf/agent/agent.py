class Agent:
    """
    Core SAAF Agent.
    """

    def __init__(self, name="SAAF-Agent"):
        self.name = name
        self.status = "initialized"

    def run(self, request):
        self.status = "running"

        response = (
            f"{self.name} received request: {request}"
        )

        self.status = "completed"

        return response