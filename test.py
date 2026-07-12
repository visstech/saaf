from memory.conversation_memory import ConversationMemory
from memory.short_term_memory import ShortTermMemory
from memory.long_term_memory import LongTermMemory
from memory.memory_manager import MemoryManager

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

memory = storage.get(
    "senthil",
    "skills"
)

print(memory)

# storage.update({
#     "user_id":"senthil",
#     "memory_key":"unknown",
#     "memory_value":{},
#     "memory_type":"test",
#     "importance":1
# })

# storage.delete(
#     "senthil",
#     "skills"
# )

 

long_term_memory = LongTermMemory(storage)


memory = {
    "user_id": "senthil",
    "memory_key": "favorite_language",
    "memory_value": {
        "language": "Python"
    },
    "memory_type": "preference",
    "importance": 10
}


long_term_memory.store(memory)
print('Using Long_term_memory:')
result = long_term_memory.recall(
    "senthil",
    "favorite_language"
)

print('Recalled from Lange term Memory:',result)

result = long_term_memory.forget("senthil",
                            "favorite_language")

if result :
    print('Memory Removed.')

print('Trying to recall after removed.')
result = long_term_memory.recall(
    "senthil",
    "favorite_language"
)
if result is None:
    print('Memory Key Not found.')
    

long_term_memory = LongTermMemory(
    storage
)


manager = MemoryManager(
    conversation_memory=None,
    short_term_memory=None,
    long_term_memory=long_term_memory
)


print("MemoryManager created successfully")


)