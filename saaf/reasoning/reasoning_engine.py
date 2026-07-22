from saaf.llm import LLMOutputParser
from saaf.validation.validator import IntentValidator
from saaf.reasoning.prompt_builder import PromptBuilder


class ReasoningEngine:
    """
    SAAF reasoning layer.

    Converts user requests into
    executable plans.
    """


    def __init__(
        self,
        llm=None,
        tools=None
    ):

        self.llm = llm
        self.tools = tools
        self.parser = LLMOutputParser()
        self.validator = IntentValidator()
        self.prompt_builder = PromptBuilder()



    def plan(
        self,
        user_request: str
    ):

        request = (
            user_request
            .lower()
            .strip()
        )


        # -----------------------------
        # LLM Reasoning
        # -----------------------------

        if self.llm:

            try:

                return self.llm_reasoning(
                    user_request
                )


            except Exception as ex:

                print(
                    "[LLM Reasoning Failed]",
                    ex
                )

                print(
                    "[Fallback] Using rules"
                )



        # -----------------------------
        # Rule Based Fallback
        # -----------------------------

        return self.rule_based_plan(
            request
        )



    # ==================================================
    # LLM PLANNING
    # ==================================================

    def llm_reasoning(
        self,
        request
    ):
        # =====================================
        # Dynamic Prompt Generation
        # =====================================
        tool_schemas = None
        if self.tools:
            tool_schemas = (
                self.tools.tool_schemas()
            )
        dynamic_prompt = (
            self.prompt_builder.build(
                tool_schemas
            )
        )
        prompt = f"""
        {dynamic_prompt}

        User request:
        {request}

        Return only JSON.

        """


        # -----------------------------
        # Call LLM
        # -----------------------------

        response = self.llm.generate_default(
            prompt
        )


        print(
            "[LLM Response]",
            response
        )


        # -----------------------------
        # Parse JSON
        # -----------------------------

        data = self.parser.parse(
            response
        )


        print(
            "[Parsed Intent]",
            data
        )


        # -----------------------------
        # Validate Intent
        # -----------------------------

        intent = self.validator.validate(
            data
        )


        print(
            "[Validated Intent]",
            intent
        )


        return intent



    # ==================================================
    # RULE ENGINE FALLBACK
    # ==================================================

    def rule_based_plan(
        self,
        request
    ):


        # -----------------------------
        # Memory Recall
        # -----------------------------

        if "last calculation" in request:

            return {

                "action":
                "memory",

                "memory_key":
                "last_calculation"

            }



        if "what is my name" in request:

            return {

                "action":
                "memory",

                "memory_key":
                "name"

            }



        # -----------------------------
        # Memory Save
        # -----------------------------

        if (
            "my name" in request
            and "is" in request
        ):

            return {

                "action":
                "memory_saved",

                "memory_key":
                "name"

            }



        if "i know" in request:

            return {

                "action":
                "memory_saved",

                "memory_key":
                "skills"

            }



        # -----------------------------
        # Calculator Workflow
        # -----------------------------

        if "calculate" in request:


            expression = (
                request
                .replace(
                    "calculate",
                    ""
                )
                .strip()
            )



            if "save" in expression:


                expression = (
                    expression
                    .split("and")[0]
                    .strip()
                )


                return {

                    "action":
                    "workflow",


                    "steps":[


                        {
                            "action":
                            "tool",

                            "tool":
                            "calculator",

                            "input":
                            expression

                        },


                        {
                            "action":
                            "save_memory",

                            "memory_key":
                            "last_calculation"

                        }

                    ]

                }



            return {

                "action":
                "tool",

                "tool":
                "calculator",

                "input":
                expression

            }



        # -----------------------------
        # Unknown
        # -----------------------------

        return {

            "action":
            "unknown",

            "input":
            request

        }