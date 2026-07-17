class AgentLoop:


    def run(self, plan, tool_manager):

        results = []


        for step in plan:

            tool_name = step["tool"]

            tool_input = step["input"]


            print(
                f"Executing tool: {tool_name}"
            )


            tool = tool_manager.get_tool(
                tool_name
            )


            result = tool.execute(
                tool_input
            )


            results.append(result)
            
            decision = observer.analyze(result)

            if decision == "RETRY":
                retry()

            elif decision == "STOP":
                finish()

            elif decision == "REPLAN":
                ask_reasoning_engine()


        return results