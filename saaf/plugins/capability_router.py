class CapabilityRouter:
    """
    Resolves capabilities into the
    best available plugin.
    """


    def __init__(
        self,
        registry
    ):

        self.registry = registry



    def resolve(
        self,
        capability
    ):
        """
        Find best enabled plugin for capability.

        Returns:
            Plugin object if available.
            None if unavailable.
        """


        plugins = (
            self.registry.find_by_capability(
                capability
            )
        )


        if not plugins:

            print(
                "[Capability Router]",
                capability,
                "-> unavailable"
            )


            return None



        # ---------------------------------
        # Select highest priority plugin
        # ---------------------------------

        plugins = sorted(

            plugins,

            key=lambda p:
                p.metadata.priority,

            reverse=True

        )


        selected = plugins[0]


        print(

            "[Capability Router]",

            capability,

            "->",

            selected.metadata.name

        )


        return selected