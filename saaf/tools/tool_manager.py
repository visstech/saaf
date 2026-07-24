from typing import Optional

from saaf.tools.base_tool import BaseTool
from saaf.tools.tool_registry import ToolRegistry
import time



class ToolManager:
    """
    Manages execution of registered SAAF tools.

    ToolManager is the execution layer.
    ToolRegistry is the storage layer.
    """


    def __init__( self,registry=None,plugin_manager=None):

        self.registry = (
            registry
            or ToolRegistry()
        )

        self.plugin_manager = plugin_manager
        

    def tool_schemas(self) -> list[dict]:
        """
        Return schemas of all registered tools.
        """

        return [
            tool.schema
            for tool in self._tools.values()
        ]

    def register_tool(
        self,
        tool: BaseTool
    ) -> None:
        """
        Register a tool.
        """

        self.registry.register(
            tool
        )



    def get_tool(
        self,
        tool_name: str
    ) -> Optional[BaseTool]:
        """
        Retrieve tool by name.
        """

        return self.registry.get(
            tool_name
        )



    def list_tools(
        self
    ):

        return self.registry.list_tools()



    def tool_schemas(
        self
    ):

        return self.registry.schemas()



    def execute_tool(
            self,
            tool_name: str,
            query: str
        ):

            tool = self.get_tool(tool_name)

            if tool is None:

                raise ValueError(
                    f"Tool '{tool_name}' not found"
                )

            start = time.perf_counter()

            try:

                result = tool.execute(query)

                elapsed = (
                    time.perf_counter()
                    - start
                )

                tool.health.record_success(
                    elapsed
                )

                return result

            except Exception as ex:

                tool.health.record_failure(
                    str(ex)
                )

                raise

    def execute_plan(
        self,
        plan: dict
    ):

        tool_name = plan.get(
            "tool"
        )


        query = plan.get(
            "input"
        )


        if not tool_name:

            raise ValueError(
                "No tool specified"
            )


        return self.execute_tool(
            tool_name,
            query
        )