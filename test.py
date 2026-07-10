from memory.conversation_memory import ConversationMemory
from memory.short_term_memory import ShortTermMemory

memory = ConversationMemory()

memory.add_message(
    "user",
    "Hello"
)

memory.add_message(
    "assistant",
    "Hello Senthil"
)

print(memory.get_history())

history = memory.get_history()

history.clear()

print("Original Memory:")
print(memory.get_history())

print('Short term memory testing:')
stm_memory = ShortTermMemory()

stm_memory.set( 
        "current_task",
        "Tesla analysis"
         )
stm_memory.set(
        "status",
        "running"
    )

print('Getting current task:',stm_memory.get("current_task"))
print('Get the current status:',stm_memory.get("status"))

stm_memory.remove("status")

print('Now get the current status:',stm_memory.get("status"))

stm_memory.clear()

print('All the Memory got cleared now:',stm_memory.memory)

from storage.base_storage import BaseStorage

print("BaseStorage imported successfully")

from config.settings import DATABASE_PATH

print(DATABASE_PATH)

from storage.sqlite_storage import SQLiteStorage


storage = SQLiteStorage()

storage.initialize()


memory = {
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

storage_id = storage.save(memory)

print("Memory saved successfully! storage_id:",storage_id)