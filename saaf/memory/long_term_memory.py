from saaf.models.memory import Memory
from saaf.storage.base_storage import BaseStorage



class LongTermMemory:
    """
    Permanent memory storage.

    Responsible for:
    - storing memories
    - recalling memories
    - forgetting memories
    """


    def __init__(self, storage: BaseStorage):
        """
        Initialize long-term memory.

        Args:
            storage: Storage implementation
        """

        self.storage = storage


    def store(self, memory: Memory):
        """
        Store memory permanently.
        """

        return self.storage.save(memory)


    def recall(self,user_id: str, memory_key: str) -> Memory | None:
        """
        Recall a stored memory.
        """

        return self.storage.get(
            user_id,
            memory_key
        )


    def forget(self,user_id: str, memory_key: str):
        """
        Forget a stored memory.
        """

        return self.storage.delete(
            user_id,
            memory_key
        )
        