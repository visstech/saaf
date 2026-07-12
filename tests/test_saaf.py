from saaf import SAAF
from models.memory import Memory


agent = SAAF()


memory = Memory(
    user_id="senthil",
    memory_key="skills",
    memory_value={
        "languages":[
            "Python",
            "SQL",
            "PyTorch"
        ]
    },
    memory_type="skill",
    importance=10
)


agent.memory.remember(memory)


result = agent.memory.recall(
    "senthil",
    "skills"
)


print(result)