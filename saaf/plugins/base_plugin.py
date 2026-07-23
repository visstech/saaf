from abc import ABC, abstractmethod

from saaf.plugins.metadata import PluginMetadata



class BasePlugin(ABC):
    """
    Base contract for all SAAF plugins.
    """


    def __init__(self):

        self.enabled = True

        self.status = "initialized"



    # =====================================
    # Plugin Metadata
    # =====================================

    @property
    @abstractmethod
    def metadata(
        self
    ) -> PluginMetadata:

        """
        Plugin information.
        """

        pass



    # =====================================
    # Tool Schema
    # =====================================

    @property
    @abstractmethod
    def schema(
        self
    ):

        """
        Tool schema exposed to reasoning engine.
        """

        pass



    # =====================================
    # Execute
    # =====================================

    @abstractmethod
    def execute(
        self,
        **kwargs
    ):

        """
        Execute plugin action.
        """

        pass



    # =====================================
    # Lifecycle Methods
    # =====================================


    def enable(self):

        self.enabled = True

        self.status = "active"



    def disable(self):

        self.enabled = False

        self.status = "disabled"



    def is_enabled(self):

        return self.enabled



    def health_check(self):

        """
        Basic plugin health check.
        Child plugins can override.
        """

        return {

            "name":
            self.metadata.name,

            "status":
            self.status,

            "enabled":
            self.enabled,

            "healthy":
            True

        }



    def initialize(self):

        """
        Called when plugin loads.
        """

        self.status = "active"