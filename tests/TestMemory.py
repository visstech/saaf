from memory.conversation_memory import ConversationMemory
from memory.short_term_memory import ShortTermMemory
from memory.long_term_memory import LongTermMemory
from memory.memory_manager import MemoryManager

from storage.sqlite_storage import SQLiteStorage


print("========== Initializing Storage ==========")

# Create Storage
storage = SQLiteStorage()

# Initialize database
storage.initialize()


print("========== Creating Memory Components ==========")

# Create Conversation Memory
conversation_memory = ConversationMemory()


# Create Short Term Memory
short_term_memory = ShortTermMemory()


# Create Long Term Memory
long_term_memory = LongTermMemory(
    storage
)


print("========== Creating Memory Manager ==========")


# Dependency Injection
manager = MemoryManager(
    conversation_memory=conversation_memory,
    short_term_memory=short_term_memory,
    long_term_memory=long_term_memory
)


print(
    "MemoryManager created successfully"
)


# ==================================================
# Test 1: Conversation Memory
# ==================================================

print("\n========== Testing Conversation Memory ==========")


conversation = {
    "memory_type": "conversation",
    "role": "user",
    "content": "Hello SAAF"
}


manager.remember(
    conversation
)


print(
    conversation_memory.get_history()
)



# ==================================================
# Test 2: Short Term Memory
# ==================================================

print("\n========== Testing Short Term Memory ==========")


task_memory = {
    "memory_type": "task",
    "memory_key": "current_task",
    "memory_value": "Tesla analysis"
}


manager.remember(
    task_memory
)


print(
    "Current Task:",
    short_term_memory.get(
        "current_task"
    )
)



# ==================================================
# Test 3: Long Term Memory
# ==================================================

print("\n========== Testing Long Term Memory ==========")


long_memory = {

    "user_id": "senthil",

    "memory_key": "skills",

    "memory_value": {
        "languages": [
            "Python",
            "SQL",
            "PyTorch"
        ]
    },

    "memory_type": "skill",

    "importance": 9
}



manager.remember(
    long_memory
)


result = long_term_memory.recall(
    "senthil",
    "skills"
)


print(
    "Long Term Memory:",
    result
)

print('This is using Recall :')
recall_result = manager.recall("senthil",
    "skills")
print(recall_result)

remove_result = manager.forget("senthil",
    "skills")

if remove_result:
    print(' Memory removed successfully')