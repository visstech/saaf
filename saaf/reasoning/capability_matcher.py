class CapabilityMatcher:
    """
    Finds the best plugin based on
    required capability.
    """


    def __init__(
        self,
        plugin_registry
    ):

        self.registry = plugin_registry



    def find_tool(
        self,
        capability: str
    ):

        plugins = self.registry.find_by_capability(
            capability
        )


        if not plugins:

            return None


        # Choose highest priority plugin

        best_plugin = max(

            plugins,

            key=lambda plugin:
            plugin.metadata.priority

        )


        return best_plugin