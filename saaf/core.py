from saaf.storage.sqlite_storage import SQLiteStorage
from saaf.memory.conversation_memory import ConversationMemory
from saaf.memory.short_term_memory import ShortTermMemory
from saaf.memory.long_term_memory import LongTermMemory
from saaf.memory.memory_manager import MemoryManager


class SAAF:
    """
    Main entry point for Smart AI Agent Framework.
    """

    def __init__(self):

        # Initialize storage

        self.storage = SQLiteStorage()

        self.storage.initialize()


        # Initialize memory components

        self.conversation_memory = ConversationMemory()

        self.short_term_memory = ShortTermMemory()


        self.long_term_memory = LongTermMemory(
            self.storage
        )


        # Create memory manager

        self.memory = MemoryManager(
            self.conversation_memory,
            self.short_term_memory,
            self.long_term_memory
        )