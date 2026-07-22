
from saaf.tools.base_tool import BaseTool
from saaf.plugins.base_plugin import BasePlugin
from saaf.plugins.metadata import PluginMetadata


class CalculatorTool(BaseTool, BasePlugin):
    
    name = "calculator"
    description = """
        Performs mathematical calculations.
        Supports:
        addition
        subtraction
        multiplication
        division
        """
    parameters = {
            "expression":"string"
        } 
    @property
    def name(self) -> str:
        return "calculator"
    
    @property
    def schema(self):

        return {

            "name": self.name,

            "description": self.description,

            "version": "1.0",

            "parameters": {

                "input": "Mathematical expression"

            },
            "category":"mathematics",
            "examples" :[
                        "calculate 25*25",
                        "what is 100/5",
                        "solve 20+30"
                        ]
            

        }

    @property
    def description(self) -> str:
        return "Performs mathematical operations like +, -, *, /"

    def execute(self, query: str):
        """
        Execute mathematical expression safely.

        Example:
            "2 + 3 * 5"
        """

        try:
            # Clean input
            expression = query.strip()

            # Evaluate math expression
            result = eval(expression)

            return {
                "tool": self.name,
                "input": query,
                "output": result
            }

        except Exception as e:
            return {
                "tool": self.name,
                "input": query,
                "error": str(e)
            }

    @property
    def metadata(self):

        return PluginMetadata(

            name="calculator",

            version="1.0",

            description=(
                "Performs mathematical "
                "operations like +, -, *, /"
            ),

            category="mathematics",

            capabilities=[

                "addition",

                "subtraction",

                "multiplication",

                "division"

            ],

            priority=10,

            cost="free",

            requires_network=False,

            supports_async=False,

            supports_streaming=False

        )
                
tool = CalculatorTool()