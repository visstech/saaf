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
        """
        Existing compatibility method.

        Returns:
            Plugin instance
            or None
        """

        plugins = (
            self.registry.find_by_capability(
                capability
            )
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




    def resolve(
        self,
        capability: str
    ):
        """
        Intelligent capability resolution.

        Returns information about
        capability availability.
        """


        plugin = self.find_tool(
            capability
        )


        # --------------------------------
        # Capability unavailable
        # --------------------------------

        if plugin is None:


            return {

                "available": False,

                "capability": capability,

                "tool": None,

                "reason":
                "No enabled plugin supports this capability."

            }



        # --------------------------------
        # Capability available
        # --------------------------------

        return {

            "available": True,

            "capability": capability,

            "tool": plugin,

            "reason": None

        }