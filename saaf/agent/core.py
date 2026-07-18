from saaf.models.memory import Memory
from saaf.memory.memory_response import MemoryResponse
from saaf.response.response_generator import ResponseGenerator
from saaf.memory.memory_extractor import MemoryExtractor

class Agent:
    """
    Core SAAF Agent.

    Responsible for managing the
    complete lifecycle and execution
    of an AI agent.
    """


    def __init__(
        self,
        name="SAAF-Agent",
        memory=None,
        reasoning=None,
        tools=None,
        observer=None,
        memory_extractor=None
    ):

        self.name = name
        self.status = "initialized"

        # Core Components
        self.memory = memory
        self.reasoning = reasoning
        self.tools = tools
        self.observer = observer
        # Response Layer
        self.response_generator = ResponseGenerator()
        self.memory_extractor = MemoryExtractor()

    def run(self, request):
        """
        Execute a user request
        through the SAAF pipeline.
        """


        self.status = "running"


        print(
            f"[Agent] Request received : {request}"
        )

        # -----------------------------
        # Memory Extraction
        # -----------------------------

        if self.memory_extractor and self.memory:

            extracted_memory = self.memory_extractor.extract(
                "default",
                request
            )


            if extracted_memory:

                self.memory.remember(
                    extracted_memory
                )

                print(
                    "[Memory Extractor] "
                    "New memory stored."
                )

                # -----------------------------
                # Observer Layer
                # -----------------------------

                if self.observer:
                    print("[Observer] Active")



        # -----------------------------
        # Memory Layer
        # -----------------------------

        if self.memory:
            print("[Memory] Connected")



        # -----------------------------
        # Reasoning Layer
        # -----------------------------

        if self.reasoning:

            print(
                "[Reasoning] Creating plan..."
            )


            plan = self.reasoning.plan(
                request
            )


            print(
                f"[Reasoning] Plan : {plan}"
            )


        else:

            plan = None



        # -----------------------------
        # Execute Plan
        # -----------------------------


        if not plan:

            result = {
                "message":
                "No plan generated."
            }


        else:


            action = plan.get(
                "action"
            )

            # -----------------------------
            # Memory Saved
            # -----------------------------

            if action == "memory_saved":

                result = {

                    "message":
                    "I have remembered that information."

                }
            
            
            # =============================
            # TOOL ACTION
            # =============================

            if action == "tool" and self.tools:


                print(
                    "[Tools] Executing..."
                )


                result = self.tools.execute_plan(
                    plan
                )



                # Save calculation result

                if (
                    self.memory
                    and isinstance(result, dict)
                    and "output" in result
                ):


                    memory = Memory(

                        user_id="default",

                        memory_key="last_calculation",

                        memory_value={

                            "expression":
                            result["input"],

                            "result":
                            result["output"]

                        },

                        memory_type="fact",

                        importance=1
                    )


                    self.memory.remember(
                        memory
                    )


                    print(
                        "[Memory] Stored calculation."
                    )


            # -----------------------------
            # Memory Saved Response
            # -----------------------------

            elif action == "memory_saved":

                result = {
                    "message":
                    "I have remembered that."
                }
            # =============================
            # MEMORY ACTION
            # =============================

           
            elif action == "memory" and self.memory:


                print(
                    "[Memory] Searching..."
                )


                memory = self.memory.recall(

                    "default",

                    plan["memory_key"]

                )


                if memory:

                     result = memory
                     
                    # result = {

                    #     "memory_key":
                    #     memory.memory_key,

                    #     "value":
                    #     memory.memory_value

                    # }


                else:


                    result = {

                        "message":
                        "I don't remember anything."

                    }



            # =============================
            # UNKNOWN ACTION
            # =============================


            else:


                result = {

                    "message":
                    "I don't know how to handle this request."

                }



        self.status = "completed"


        return self.response_generator.generate(result)



    def recall(
        self,
        user_id,
        memory_key
    ):
        """
        Retrieve stored memory.
        """


        if not self.memory:

            return None


        return self.memory.recall(

            user_id,

            memory_key

        )



    def recall_response(
        self,
        user_id,
        memory_key
    ):
        """
        Retrieve memory as natural response.
        """


        memory = self.recall(

            user_id,

            memory_key

        )


        return MemoryResponse.format(
            memory
        )