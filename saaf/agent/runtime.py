from saaf.memory.memory_manager import MemoryManager
from saaf.memory.conversation_memory import ConversationMemory
from saaf.memory.short_term_memory import ShortTermMemory
from saaf.memory.long_term_memory import LongTermMemory

from saaf.storage.sqlite_storage import SQLiteStorage

from saaf.reasoning.reasoning_engine import ReasoningEngine
from saaf.reasoning.planner import Planner

from saaf.tools.tool_manager import ToolManager
from saaf.tools.calculator_tool import CalculatorTool

from saaf.observer.observer import Observer

from saaf.memory.memory_extractor import MemoryExtractor


# Temporary Executor (we will remove later)
from saaf.runtime.executor import Executor


# Workflow System
from saaf.workflow.workflow import WorkflowEngine
from saaf.workflow.registry import WorkflowRegistry

from saaf.workflow.nodes.calculator_node import CalculatorNode
from saaf.workflow.nodes.memory_node import MemoryNode



def create_runtime():

    """
    Creates complete SAAF runtime environment.

    Initializes:

    - Storage
    - Memory
    - Tools
    - Reasoning
    - Planner
    - Workflow
    - Observer
    """



    # =====================================
    # Storage Layer
    # =====================================

    storage = SQLiteStorage()



    # =====================================
    # Memory Layer
    # =====================================

    conversation_memory = ConversationMemory()


    short_term_memory = ShortTermMemory()


    long_term_memory = LongTermMemory(
        storage
    )


    memory_manager = MemoryManager(

        conversation_memory,

        short_term_memory,

        long_term_memory

    )



    # =====================================
    # Tool Layer
    # =====================================

    tool_manager = ToolManager()


    calculator = CalculatorTool()


    tool_manager.register_tool(
        calculator
    )



    # =====================================
    # Reasoning Layer
    # =====================================

    reasoning_engine = ReasoningEngine()


    planner = Planner()



    # =====================================
    # Memory Extraction
    # =====================================

    memory_extractor = MemoryExtractor()



    # =====================================
    # Observer
    # =====================================

    observer = Observer()



    # =====================================
    # Workflow Registry
    # =====================================

    registry = WorkflowRegistry()



    # Register Workflow Nodes

    registry.register(

        "execute_tool",

        CalculatorNode(
            tool_manager
        )

    )


    registry.register(

        "save_memory",

        MemoryNode(
            memory_manager
        )

    )



    # =====================================
    # Workflow Engine
    # =====================================

    workflow = WorkflowEngine(

        registry

    )



    # =====================================
    # Old Executor
    # Temporary
    # =====================================

    executor = Executor(

        tools=tool_manager,

        memory=memory_manager

    )



    # =====================================
    # Runtime Objects
    # =====================================

    return {


        "memory":
        memory_manager,


        "reasoning":
        reasoning_engine,


        "tools":
        tool_manager,


        "observer":
        observer,


        "memory_extractor":
        memory_extractor,


        "planner":
        planner,


        # Temporary
        "executor":
        executor,


        # New Workflow Engine
        "workflow":
        workflow,


        # Registry access
        "registry":
        registry

    }