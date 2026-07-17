class ShortTermMemory:

    def __init__(self):
        self.memory = {}


    def set(self, key, value):
        self.memory[key] = value


    def get(self, key):
        return self.memory.get(key)


    def remove(self, key):
        if key in self.memory:
            del self.memory[key]


    def clear(self):
        self.memory.clear()