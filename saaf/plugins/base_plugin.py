from abc import ABC, abstractmethod

from saaf.plugins.metadata import PluginMetadata
from saaf.plugins.plugin_health import PluginHealth



class BasePlugin(ABC):
    """
    Base contract for all SAAF plugins.
    """


    def __init__(self):
        
        
        self.enabled = True

        self.status = "initialized"
        self.health = PluginHealth()



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
        self.health.enabled = True



    def disable(self):

        self.enabled = False

        self.status = "disabled"
        self.health.enabled = False



    def is_enabled(self):

        return self.enabled



    def health_check(self):

            return {

                "name": self.metadata.name,

                "status": self.status,

                "enabled": self.enabled,

                "healthy": self.health.healthy,

                "success_count": self.health.success_count,

                "failure_count": self.health.failure_count,

                "average_response_time":
                    round(
                        self.health.average_response_time,
                        4
                    ),

                "last_error": self.health.last_error

            }


    def initialize(self):

        """
        Called when plugin loads.
        """

        self.status = "active"
        self.health.enabled = True