from abc import ABC, abstractmethod


class BaseFormatter(ABC):
    """
    Base class for all response formatters.

    Every formatter converts a tool's raw output
    into a human-readable response.
    """


    @property
    @abstractmethod
    def tool_name(self) -> str:
        """
        Name of the tool this formatter supports.

        Example:
            calculator
            weather
            stock
        """
        pass


    @abstractmethod
    def format(self, result: dict) -> str:
        """
        Convert tool output into a readable response.

        Args:
            result : Tool execution result

        Returns:
            str
        """
        pass