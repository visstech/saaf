class PromptBuilder:
    """
    Builds dynamic prompts for LLM.

    Converts tool/plugin schemas into
    LLM understandable instructions.

    Supports:
    - Tool information
    - Plugin capabilities
    - Parameters
    - Examples
    """


    def build(
        self,
        tools=None
    ):

        prompt = """

You are SAAF Agent.

Your task is to understand the user request
and select the correct action.

You should reason using available capabilities.

Available tools:

"""


        # =====================================
        # No tools available
        # =====================================

        if not tools:

            prompt += """

No external tools are available.

"""


        else:


            # =====================================
            # Tool Details
            # =====================================

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


Capabilities:
"""


                # -----------------------------
                # Capabilities
                # -----------------------------

                for capability in tool.get(
                    "capabilities",
                    []
                ):

                    prompt += (
                        f"- {capability}\n"
                    )


                prompt += """

Parameters:
"""


                # -----------------------------
                # Parameters
                # -----------------------------

                for key, value in tool.get(
                    "parameters",
                    {}
                ).items():

                    prompt += (
                        f"- {key}: {value}\n"
                    )


                # -----------------------------
                # Examples
                # -----------------------------

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



        # =====================================
        # JSON Output Instructions
        # =====================================

        prompt += """

Return ONLY valid JSON.

Use capability instead of tool name whenever possible.


Example 1:

User:
calculate 10*20


Output:

{
 "action":"tool",
 "capability":"multiplication",
 "input":"10*20"
}



Example 2:

User:
what is the weather in Kuala Lumpur


Output:

{
 "action":"tool",
 "capability":"weather",
 "input":"Kuala Lumpur"
}



Example 3:

User:
what is the forecast tomorrow


Output:

{
 "action":"tool",
 "capability":"forecast",
 "input":"tomorrow"
}



Example 4:

For multiple actions:


{
 "action":"workflow",
 "steps":[

    {
      "action":"tool",
      "capability":"multiplication",
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