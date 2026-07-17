# tools/tool_manager.py

from typing import Dict, Optional

from saaf.tools.base_tool import BaseTool


class ToolManager:
    """
    Registers and manages all tools used by the AI Agent.
    """

    def __init__(self):
        self._tools: Dict[str, BaseTool] = {} # "This dictionary will have string keys and BaseTool objects as values."

    def register_tool(self, tool: BaseTool) -> None:
        """
        Register a tool using its unique name.
        """
        if tool.name in self._tools:
            raise ValueError(f"Tool '{tool.name}' already registered" )
        else:           
            self._tools[tool.name] = tool

    def get_tool(self, tool_name: str) -> Optional[BaseTool]:
        """
        Return the requested tool.
        """
        return self._tools.get(tool_name)

    def list_tools(self) -> list[str]:
        """
        Return all registered tool names.
        """
        return list(self._tools.keys())

    def execute_tool(self, tool_name: str, query: str):
        """
        Execute a tool by name.
        """
        tool = self.get_tool(tool_name)

        if tool is None:
            raise ValueError(f"Tool '{tool_name}' not found.")

        return tool.execute(query)