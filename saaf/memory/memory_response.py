class MemoryResponse:

    @staticmethod
    def format(memory):

        if memory is None:
            return "I don't remember anything."

        if memory.memory_key == "last_calculation":

            data = memory.memory_value

            return (
                f"Your last calculation was "
                f"{data['expression']} = "
                f"{data['result']}"
            )


        return str(memory.memory_value)