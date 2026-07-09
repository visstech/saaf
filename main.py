from tools.tool_manager import ToolManager
from tools.calculator_tool import CalculatorTool
from agent.agent import AIAgent


def main():
    manager = ToolManager()

    print("AI Agent Tool Manager Started")
    calculator = CalculatorTool()

    manager.register_tool(calculator)

    print("Available Tools:")
    print(manager.list_tools())
    
    agent = AIAgent()

    agent.process_request(
        "Calculate 25 * 20"
    )

    result = manager.execute_tool(
        "calculator",
        "25 * 20"
    )

    print(result)

if __name__ == "__main__":
    main()