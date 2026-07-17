from saaf.memory.memory_manager import MemoryManager
from saaf.memory.conversation_memory import ConversationMemory
from saaf.memory.short_term_memory import ShortTermMemory
from saaf.memory.long_term_memory import LongTermMemory

from saaf.storage.sqlite_storage import SQLiteStorage

from saaf.reasoning.reasoning_engine import ReasoningEngine

from saaf.tools.tool_manager import ToolManager
from saaf.tools.calculator_tool import CalculatorTool

from saaf.observer.observer import Observer


def create_runtime():

    # Storage
    storage = SQLiteStorage()


    # Memory Layer
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


    # Tools
    tool_manager = ToolManager()

    calculator = CalculatorTool()

    tool_manager.register_tool(
    calculator
                              )


    # Reasoning
    reasoning_engine = ReasoningEngine()


    # Observer
    observer = Observer()


    return {
        "memory": memory_manager,
        "reasoning": reasoning_engine,
        "tools": tool_manager,
        "observer": observer
    }