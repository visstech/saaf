from abc import ABC, abstractmethod

from saaf.plugins.metadata import PluginMetadata



class BasePlugin(ABC):
    """
    Base contract for all SAAF plugins.
    """


    @property
    @abstractmethod
    def metadata(
        self
    ) -> PluginMetadata:
        """
        Plugin information.
        """
        pass



    @abstractmethod
    def schema(
        self
    ):
        """
        Tool schema exposed to reasoning engine.
        """
        pass



    @abstractmethod
    def execute(
        self,
        **kwargs
    ):
        """
        Execute plugin action.
        """
        pass