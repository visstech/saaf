from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Base interface for all LLM providers.
    """

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def generate(
        self,
        prompt: str
    ):
        """
        Generate response from LLM.
        """
        pass