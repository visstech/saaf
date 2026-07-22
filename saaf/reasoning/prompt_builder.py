class PromptBuilder:
    """
    Builds dynamic prompts for LLM.

    Converts tool schemas into
    LLM understandable instructions.
    """

    def build(
        self,
        tools=None
    ):

        prompt = """

You are SAAF Agent.

Your task is to understand the user request
and select the correct action.

Available tools:

"""


        if not tools:

            prompt += """

No external tools are available.

"""


        else:

            for index, tool in enumerate(
                tools,
                start=1
            ):

                prompt += f"""

Tool {index}:

Name:
{tool['name']}

Description:
{tool['description']}

Version:
{tool.get('version','unknown')}

Category:
{tool.get('category','general')}

Parameters:
"""


                for key, value in tool.get(
                    "parameters",
                    {}
                ).items():

                    prompt += (
                        f"- {key}: {value}\n"
                    )


                prompt += """

Examples:
"""


                for example in tool.get(
                    "examples",
                    []
                ):

                    prompt += (
                        f"- {example}\n"
                    )



        prompt += """

Return ONLY valid JSON.

Available actions:

1. tool
2. workflow
3. memory
4. memory_saved
5. unknown


Example:

For calculator:

{
 "action":"tool",
 "tool":"calculator",
 "input":"10*20"
}


For workflow:

{
 "action":"workflow",
 "steps":[

    {
     "action":"tool",
     "tool":"calculator",
     "input":"10*20"
    },

    {
     "action":"save_memory",
     "memory_key":"last_calculation"
    }

 ]
}

"""


        return prompt