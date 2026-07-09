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
        """
        Unique name of the tool
        Example: 'calculator', 'weather'
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Human-readable description of the tool.
        Helps LLM decide which tool to use.
        """
        pass

    @abstractmethod
    def execute(self, query: str):
        """
        Main function that runs the tool logic.

        Args:
            query (str): Input from user or agent

        Returns:
            Any: Result of tool execution
        """
        pass