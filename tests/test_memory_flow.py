from models.memory import Memory

from storage.sqlite_storage import SQLiteStorage

from memory.long_term_memory import LongTermMemory
from memory.memory_manager import MemoryManager

from memory.conversation_memory import ConversationMemory
from memory.short_term_memory import ShortTermMemory



print("Starting SAAF Memory Integration Test")


# 1. Create Storage

storage = SQLiteStorage()

storage.initialize()


# 2. Create Memory Components

conversation_memory = ConversationMemory()

short_term_memory = ShortTermMemory()

long_term_memory = LongTermMemory(
    storage
)


# 3. Create Memory Manager

manager = MemoryManager(
    conversation_memory,
    short_term_memory,
    long_term_memory
)


print("MemoryManager created successfully")


# ======================================
# Test 1: Store Long Term Memory
# ======================================

print("\nTesting remember()")


memory = Memory(
    user_id="senthil",
    memory_key="skills",
    memory_value={
        "languages": [
            "Python",
            "SQL",
            "PyTorch"
        ]
    },
    memory_type="skill",
    importance=9
)


manager.remember(memory)


print("Memory stored successfully")


# ======================================
# Test 2: Recall Memory
# ======================================

print("\nTesting recall()")


result = manager.recall(
    "senthil",
    "skills"
)


print(result)


print(
    result.memory_value
)


# ======================================
# Test 3: Forget Memory
# ======================================

print("\nTesting forget()")


deleted = manager.forget(
    "senthil",
    "skills"
)


print(
    "Deleted:",
    deleted
)


# Verify deletion

result = manager.recall(
    "senthil",
    "skills"
)


print(
    "After delete:",
    result
)


print("\nSAAF Memory Integration Test Completed")