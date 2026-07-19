from saaf.llm.base_llm import BaseLLM


class LLMManager:


    def __init__(
        self,
        default="reasoning"
    ):

        self.models = {}

        self.default = default



    def register(
        self,
        name,
        llm
    ):

        self.models[name] = llm



    def get(
        self,
        name=None
    ):

        if name is None:

            name = self.default


        return self.models.get(
            name
        )



    def generate(
        self,
        name,
        prompt
    ):

        llm = self.get(
            name
        )


        if llm is None:

            raise Exception(
                f"LLM {name} not found"
            )


        return llm.generate(
            prompt
        )



    def generate_default(
        self,
        prompt
    ):
        """
        Used by Agent reasoning.
        """

        llm = self.get()


        if llm is None:

            raise Exception(
                "Default LLM unavailable"
            )


        return llm.generate(
            prompt
        )



    def list_models(self):

        return list(
            self.models.keys()
        )