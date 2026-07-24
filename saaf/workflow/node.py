from abc import ABC, abstractmethod


class WorkflowNode(ABC):
    """
    Base class for workflow steps.
    """


    name = "base"



    @abstractmethod
    def execute(
        self,
        state
    ):

        pass