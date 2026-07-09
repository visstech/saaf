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
