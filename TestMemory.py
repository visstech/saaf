from models.memory import Memory
from storage.sqlite_storage import SQLiteStorage
from memory.long_term_memory import LongTermMemory

storage = SQLiteStorage() 
storage.initialize()

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

print(memory)
storage.save(memory)
print('From get method:')
get_result = storage.get('senthil','skills')
print(get_result)

print(memory)

print(type(memory))

print(memory.memory_key)

print(memory.memory_value)

memory = Memory(
    user_id="senthil",
    memory_key="skills",
    memory_value={
        "languages":[
            "Python",
            "SQL",
            "PyTorch",
            "LangChain"
        ]
    },
    memory_type="skill",
    importance=10
)
print('Memory is getting updated:')
storage.update(memory)
result = storage.get(
    "senthil",
    "skills"
)

print(result)
print(result.memory_value)

print('Testing Long Term Memory:')
memory = Memory(
    user_id="Aruthra",
    memory_key="skills",
    memory_value={
        "languages":[
            "Python",
            "SQL",
            "PyTorch"
        ]
    },
    memory_type="skill",
    importance=9
)

LN_Memory = LongTermMemory(storage=storage)
LN_Memory.store(memory)

result = LN_Memory.recall(
    "Aruthra",
    "skills"
)

print(result)

print(
    result.memory_value
)