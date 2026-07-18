"""
SAAF Agent Interface.

High level agent that initializes
the SAAF runtime environment.
"""


from .core import Agent as CoreAgent
from .runtime import create_runtime



class SAAFAgent(CoreAgent):
    """
    High level SAAF Agent.

    Creates and manages the
    internal SAAF components.
    """


    def __init__(
        self,
        name="SAAF-Agent",
        memory=None,
        reasoning=None,
        tools=None,
        observer=None,
        planner=None,
        executor=None,
        memory_extractor=None,
        workflow=None
    ):


        # Create default runtime

        runtime = create_runtime()



        # Runtime dependency injection

        if memory is None:
            memory = runtime["memory"]


        if reasoning is None:
            reasoning = runtime["reasoning"]


        if tools is None:
            tools = runtime["tools"]


        if observer is None:
            observer = runtime["observer"]


        if planner is None:
            planner = runtime["planner"]


        if executor is None:
            executor = runtime["executor"]


        if memory_extractor is None:
            memory_extractor = runtime["memory_extractor"]
        
        if workflow is None:
            workflow = runtime["workflow"]



        super().__init__(

            name=name,

            memory=memory,

            reasoning=reasoning,

            tools=tools,

            observer=observer,

            planner=planner,

            executor=executor,

            memory_extractor=memory_extractor,
            
            workflow=workflow
        )



    def info(self):

        return {

            "name": self.name,

            "status": self.status,

            "memory":
            type(self.memory).__name__,

            "reasoning":
            type(self.reasoning).__name__,

            "tools":
            type(self.tools).__name__,

            "planner":
            type(self.planner).__name__,

            "executor":
            type(self.executor).__name__,

            "observer":
            type(self.observer).__name__

        }