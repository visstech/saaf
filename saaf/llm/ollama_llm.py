from ollama import chat

from saaf.llm.base_llm import BaseLLM


class OllamaLLM(BaseLLM):

    def __init__(self, model="llama3"):

        self.model = model

    @property
    def name(self):

        return "ollama"

    def generate(self, prompt):

        try:

            response = chat(

                model=self.model,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception as ex:

            return f"Ollama Error : {ex}"