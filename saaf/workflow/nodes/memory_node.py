from saaf.workflow.node import WorkflowNode
from saaf.models.memory import Memory



class MemoryNode(WorkflowNode):


    name = "memory"



    def __init__(
        self,
        memory
    ):

        self.memory = memory



    def execute(
        self,
        state,
        step
    ):


        value = state.get(
            "last_result"
        )


        memory = Memory(

            user_id=state.user_id,

            memory_key=step["memory_key"],

            memory_value=value,

            memory_type="fact",

            importance=1
        )


        self.memory.remember(
            memory
        )


        state.add_result(
            {
                "memory_saved":
                True
            }
        )


        return state