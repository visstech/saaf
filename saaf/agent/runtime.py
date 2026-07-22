from saaf.memory.memory_manager import MemoryManager
from saaf.memory.conversation_memory import ConversationMemory
from saaf.memory.short_term_memory import ShortTermMemory
from saaf.memory.long_term_memory import LongTermMemory

from saaf.storage.sqlite_storage import SQLiteStorage

from saaf.reasoning.reasoning_engine import ReasoningEngine
from saaf.reasoning.planner import Planner

from saaf.tools.tool_manager import ToolManager 
from saaf.tools.plugin_loader import PluginLoader

from saaf.observer.observer import Observer

from saaf.memory.memory_extractor import MemoryExtractor
from saaf.llm import (LLMManager, OllamaLLM)
# Workflow System
from saaf.workflow.workflow import WorkflowEngine
from saaf.workflow.registry import WorkflowRegistry

#from saaf.workflow.nodes.calculator_node import CalculatorNode
from saaf.workflow.nodes.memory_node import MemoryNode
from saaf.workflow.nodes.tool_node import ToolNode

from saaf.response.formatter_registry import FormatterRegistry

from saaf.response.formatters.calculator_formatter import CalculatorFormatter
from saaf.response.formatters.weather_formatter import WeatherFormatter
from saaf.response.formatter_loader import FormatterLoader



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
    
    plugin_loader = PluginLoader()

    plugins = plugin_loader.load_plugins()


    for tool in plugins:

        tool_manager.register_tool(
            tool
        )
    

    # -----------------------------
    # LLM Layer
    # -----------------------------

    llm_manager = LLMManager()


    llm_manager.register("fast",
                 OllamaLLM(model="phi3"))


    llm_manager.register("reasoning",
               OllamaLLM(model="deepseek-r1"))


    # =====================================
    # Reasoning Layer
    # =====================================

    reasoning_engine = ReasoningEngine(
            llm=llm_manager,
            tools=tool_manager
        )     


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
            ToolNode(tool_manager))


    registry.register("save_memory",
        MemoryNode(memory_manager))



    # =====================================
    # Workflow Engine
    # =====================================

    workflow = WorkflowEngine(

        registry

    )

    formatter_registry = FormatterRegistry()

    loader = FormatterLoader()

    for formatter in loader.load_formatters():

        formatter_registry.register(
            formatter
        )


    # =====================================
    # Old Executor
    # Temporary
    # =====================================

    # executor = Executor(
    #     tools=tool_manager,
    #     memory=memory_manager)



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
        # New Workflow Engine
        "workflow":
        workflow,
        # Registry access
        "registry":
        registry,        
        "llm": llm_manager,
        "formatter_registry": formatter_registry

    }