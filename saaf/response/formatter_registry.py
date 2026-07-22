from typing import Dict, Optional

from saaf.response.formatters.base_formatter import BaseFormatter



class FormatterRegistry:
    """
    Registry responsible for managing
    response formatters.

    Maps tool names to formatter objects.
    """


    def __init__(self):

        self._formatters: Dict[str, BaseFormatter] = {}



    def register(
        self,
        formatter: BaseFormatter
    ) -> None:
        """
        Register a formatter.
        """

        name = formatter.tool_name


        if name in self._formatters:

            raise ValueError(
                f"Formatter '{name}' already registered"
            )


        self._formatters[name] = formatter




    def get_formatter(
        self,
        tool_name: str
    ) -> Optional[BaseFormatter]:
        """
        Get formatter by tool name.
        """

        return self._formatters.get(
            tool_name
        )




    def list_formatters(
        self
    ) -> list[str]:
        """
        List all registered formatter names.
        """

        return list(
            self._formatters.keys()
        )




    def format(
        self,
        result: dict
    ):
        """
        Find formatter and generate response.
        """

        tool_name = result.get(
            "tool"
        )


        formatter = self.get_formatter(
            tool_name
        )


        if formatter is None:

            return None


        return formatter.format(
            result
        )