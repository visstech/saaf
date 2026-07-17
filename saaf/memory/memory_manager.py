from saaf.models.memory import Memory
from typing import Any

class MemoryManager:
    """
    Central coordinator for SAAF memory.

    Responsible for routing memory
    between conversation, short-term,
    and long-term memory.
    """

    def __init__(
        self,
        conversation_memory,
        short_term_memory,
        long_term_memory
    ):

        self.conversation_memory = conversation_memory

        self.short_term_memory = short_term_memory

        self.long_term_memory = long_term_memory
        
    def remember(self,memory: Memory) -> Any:
        """
        Store memory based on memory type.
        """

        if memory.memory_type == "conversation":
            conversation = memory.memory_value
            return self.conversation_memory.add_message(
                                conversation["role"],
                                conversation["content"]
                            )


        elif memory.memory_type in [
            "skill",
            "preference",
            "fact"
        ]:

            return self.long_term_memory.store(
                memory
            )


        else:

            return self.short_term_memory.set(
                memory.memory_key,
                memory.memory_value
            )
        
            
    def recall(self,user_id: str, memory_key: str) -> Any | None:
        """
        Retrieve memory.

        Priority:
        1. Long-term memory
        2. Short-term memory
        3. Conversation memory
        """

        # 1. Search Long Term Memory

        result = self.long_term_memory.recall(
            user_id,
            memory_key
        )


        if result is not None:
            return result


        # 2. Search Short Term Memory

        result = self.short_term_memory.get(
            memory_key
        )


        if result is not None:
            return result


        # 3. Search Conversation Memory

        history = self.conversation_memory.get_history()


        for message in reversed(history):

            if message.get("content") == memory_key:
                return message


        return None
    
    def forget(self, user_id: str, memory_key: str) -> bool:
        """
        Remove a long-term memory.
        """

        return self.long_term_memory.forget(
                user_id,
                memory_key)