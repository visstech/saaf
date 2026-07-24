class CapabilityMatcher:
    """
    Finds the best plugin based on
    required capability.

    Health aware capability resolver.
    """


    def __init__(
        self,
        plugin_registry
    ):

        self.registry = plugin_registry



    # ==================================================
    # Find Plugin
    # ==================================================

    def find_tool(
        self,
        capability: str
    ):
        """
        Returns the best available
        healthy plugin.
        """


        plugins = (
            self.registry.find_by_capability(
                capability
            )
        )


        if not plugins:

            return None



        # --------------------------------
        # Filter enabled + healthy plugins
        # --------------------------------

        available_plugins = [

            plugin

            for plugin in plugins

            if plugin.enabled

            and plugin.health_check().get(
                "healthy",
                False
            )

        ]



        if not available_plugins:

            return None



        # --------------------------------
        # Highest priority selection
        # --------------------------------

        best_plugin = max(

            available_plugins,

            key=lambda plugin:
                plugin.metadata.priority

        )


        print(
            "[Capability Matcher]",
            capability,
            "->",
            best_plugin.metadata.name
        )


        return best_plugin




    # ==================================================
    # Resolve Capability
    # ==================================================

    def resolve(
        self,
        capability: str
    ):
        """
        Intelligent capability resolution.

        Returns capability status.
        """


        plugin = self.find_tool(
            capability
        )



        # --------------------------------
        # No healthy plugin
        # --------------------------------

        if plugin is None:


            print(
                "[Capability Matcher]",
                capability,
                "-> unavailable"
            )


            return {

                "available": False,

                "capability": capability,

                "tool": None,

                "reason":
                "No enabled healthy plugin supports this capability."

            }



        # --------------------------------
        # Available
        # --------------------------------

        return {

            "available": True,

            "capability": capability,

            "tool": plugin,

            "reason": None

        }