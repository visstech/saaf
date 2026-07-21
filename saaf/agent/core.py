from saaf.models.memory import Memory
from saaf.memory.memory_response import MemoryResponse
from saaf.response.response_generator import ResponseGenerator
from saaf.memory.memory_extractor import MemoryExtractor
from saaf.workflow.state import WorkflowState



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
        memory_extractor=None,
        planner=None,        
        workflow=None
    ):

        self.name = name
        self.status = "initialized"

        self.memory = memory
        self.reasoning = reasoning
        self.tools = tools
        self.observer = observer
        self.workflow = workflow

        self.response_generator = ResponseGenerator()

        self.memory_extractor = (
            memory_extractor
            or MemoryExtractor()
        )

        self.planner = planner
       



    def run(self, request):

        self.status = "running"


        print(
            f"[Agent] Request received : {request}"
        )


        # =============================
        # Memory Extraction
        # =============================

        if self.memory_extractor and self.memory:


            extracted_memory = (
                self.memory_extractor.extract(
                    "default",
                    request
                )
            )


            if extracted_memory:

                self.memory.remember(
                    extracted_memory
                )


                print(
                    "[Memory Extractor] New memory stored."
                )



        # =============================
        # Observer
        # =============================

        if self.observer:

            print(
                "[Observer] Active"
            )



        # =============================
        # Memory Layer
        # =============================

        if self.memory:

            print(
                "[Memory] Connected"
            )



        # =============================
        # Reasoning
        # =============================

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



        # =============================
        # Execute Plan
        # =============================

        if not plan:

            result = {
                "message":
                "No plan generated."
            }


        else:


            if isinstance(plan, dict):

                action = plan.get("action")

            else:

                action = plan.action



            # =============================
            # Memory Saved
            # =============================

            if action == "memory_saved":


                result = {

                    "message":
                    "I have remembered that."

                }



            # =============================
            # TOOL / WORKFLOW
            # =============================

            elif action in [
                "tool",
                "workflow"
            ]:


                if not self.planner or not self.workflow:

                    result = {

                        "message":
                        "Workflow not available."

                    }


                else:


                    print(
                        "[Planner] Creating execution plan..."
                    )


                    execution_plan = (
                        self.planner.create_plan(
                            plan
                        )
                    )


                    print(
                        f"[Planner] Plan : {execution_plan}"
                    )


                    print(
                        "[workflow] Executing..."
                    )

                    state = WorkflowState(
                            user_id="default",
                            request=request
                        )
                    
                    context = (
                        self.workflow.run(
                            execution_plan,
                            state
                        )
                    )


                    print(
                        "[Workflow  Output]",
                        context
                    )



                    # -------------------------
                    # Store calculator result
                    # -------------------------

                    for item in context.results:


                        if (

                            isinstance(item, dict)

                            and item.get("tool")
                            == "calculator"

                            and "output" in item

                        ):


                            memory = Memory(

                                user_id="default",

                                memory_key="last_calculation",

                                memory_value={

                                    "expression":
                                    item["input"],

                                    "result":
                                    item["output"]

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



                    # -------------------------
                    # Final result
                    # -------------------------

                    if context.results:

                        result = context.results


                    else:

                        result = {

                            "message":
                            "Execution returned no result."

                        }





            # =============================
            # MEMORY SEARCH
            # =============================

            elif action == "memory":


                print(
                    "[Memory] Searching..."
                )


                memory = self.memory.recall(

                    "default",

                    plan["memory_key"]

                )


                if memory:

                    result = memory


                else:

                    result = {

                        "message":
                        "I don't remember anything."

                    }



            # =============================
            # UNKNOWN
            # =============================

            else:

                result = {

                    "message":
                    "I don't know how to handle this request."

                }



        self.status = "completed"


        return self.response_generator.generate(
            result
        )



    def recall(
        self,
        user_id,
        memory_key
    ):


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


        memory = self.recall(
            user_id,
            memory_key
        )


        return MemoryResponse.format(
            memory
        )