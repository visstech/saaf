from abc import abstractmethod
from saaf.plugins.base_plugin import BasePlugin


class BaseTool(BasePlugin):
    """
    Base class for SAAF executable tools.
    """


    def __init__(self):

        super().__init__()

        self.parameters = {}

        self.examples = []



    @property
    @abstractmethod
    def name(self) -> str:

        pass



    @property
    @abstractmethod
    def description(self) -> str:

        pass



    @property
    def version(self):

        return "1.0"



    @property
    def category(self):

        return "general"



    def schema(self):

        return {

            "name":
            self.name,

            "description":
            self.description,

            "version":
            self.version,

            "category":
            self.category,

            "parameters":
            self.parameters,

            "examples":
            self.examples

        }



    @abstractmethod
    def execute(
        self,
        query: str
    ):

        pass