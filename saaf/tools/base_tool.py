from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Abstract base class for all tools in the AI Agent system.

    Every tool MUST follow this structure:
    - name (identifier)
    - description (what it does)
    - execute() (main logic)
    """

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



    def schema(self):

        return {

            "name": self.name,

            "description":
            self.description,

            "version":
            self.version

        }


    @abstractmethod
    def execute(
        self,
        query: str
    ):

        pass