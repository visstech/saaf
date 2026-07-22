from typing import Dict

from saaf.tools.base_tool import BaseTool



class ToolRegistry:
    """
    Stores available SAAF tools.
    """


    def __init__(self):

        self.tools: Dict[str, BaseTool] = {}



    def register(
        self,
        tool: BaseTool
    ):

        self.tools[tool.name] = tool



    def get(
        self,
        name
    ):

        return self.tools.get(name)



    def list_tools(self):

        return list(
            self.tools.keys()
        )



    def schemas(self):

        return [

            tool.schema

            for tool in self.tools.values()

        ]