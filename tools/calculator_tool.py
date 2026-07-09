from tools.base_tool import BaseTool


class CalculatorTool(BaseTool):
    """
    Tool for performing basic mathematical calculations.
    """

    @property
    def name(self) -> str:
        return "calculator"

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