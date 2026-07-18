from saaf.workflow.state import WorkflowState
from saaf.workflow.workflow import WorkflowEngine
from saaf.workflow.tool_node import ToolNode
from saaf.workflow.memory_node import MemoryNode

from saaf.tools.tool_manager import ToolManager
from saaf.tools.calculator_tool import CalculatorTool

from saaf.memory.memory_manager import MemoryManager
from saaf.agent.runtime import create_runtime

manager = ToolManager()

manager.register_tool(
    CalculatorTool()
)

tool_node = ToolNode(
    manager
)

runtime = create_runtime()

memory_node = MemoryNode(
    runtime["memory"]
)

workflow = WorkflowEngine(

    nodes={

        "execute_tool":
        tool_node,

        "save_memory":
        memory_node

    }

)

state = WorkflowState(

    user_id="default",

    request="calculate 20*30"

)

plan = [

{
    "step":1,

    "action":"execute_tool",

    "tool":"calculator",

    "input":"20*30"

},

{

    "step":2,

    "action":"save_memory",

    "memory_key":"last_calculation"

}

]

result = workflow.run(
    plan,
    state
)


print(result)