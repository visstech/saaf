from typing import Dict

from saaf.plugins.base_plugin import BasePlugin



class PluginRegistry:
    """
    Stores SAAF plugins
    and provides plugin intelligence.
    """


    def __init__(self):

        self.plugins: Dict[str, BasePlugin] = {}



    # =====================================
    # Register Plugin
    # =====================================

    def register(
        self,
        plugin: BasePlugin
    ):

        name = plugin.metadata.name


        self.plugins[name] = plugin


        print(
            f"[Plugin Registry] Registered: {name}"
        )



    # =====================================
    # Get Plugin
    # =====================================

    def get(
        self,
        name: str
    ):

        return self.plugins.get(
            name
        )



    # =====================================
    # List Plugins
    # =====================================

    def list_plugins(self):

        return [

            {
                "name":
                plugin.metadata.name,


                "version":
                plugin.metadata.version,


                "description":
                plugin.metadata.description,


                "category":
                plugin.metadata.category,


                "capabilities":
                plugin.metadata.capabilities,


                "priority":
                plugin.metadata.priority,


                "requires_network":
                plugin.metadata.requires_network,


                "status":
                plugin.status,


                "enabled":
                plugin.enabled

            }

            for plugin in self.plugins.values()

        ]



    # =====================================
    # Find By Capability
    # =====================================

    def find_by_capability(
        self,
        capability: str
    ):

        matches = []


        for plugin in self.plugins.values():


            if capability in plugin.metadata.capabilities:

                if plugin.enabled:

                    matches.append(
                        plugin
                    )


        return matches



    # =====================================
    # Enable Plugin
    # =====================================

    def enable_plugin(
        self,
        name: str
    ):

        plugin = self.get(
            name
        )


        if not plugin:

            return {

                "success": False,

                "message":
                f"Plugin {name} not found."

            }



        plugin.enable()


        return {

            "success": True,

            "message":
            f"{name} enabled."

        }



    # =====================================
    # Disable Plugin
    # =====================================

    def disable_plugin(
        self,
        name: str
    ):

        plugin = self.get(
            name
        )


        if not plugin:

            return {

                "success": False,

                "message":
                f"Plugin {name} not found."

            }



        plugin.disable()


        return {

            "success": True,

            "message":
            f"{name} disabled."

        }



    # =====================================
    # Plugin Status
    # =====================================

    def plugin_status(
        self,
        name: str
    ):

        plugin = self.get(
            name
        )


        if not plugin:

            return None



        return plugin.health_check()



    # =====================================
    # Health Report
    # =====================================

    def health_report(
        self
    ):


        return [

            plugin.health_check()

            for plugin in self.plugins.values()

        ]



    # =====================================
    # Metadata
    # =====================================

    def metadata(
        self
    ):

        return [

            plugin.metadata

            for plugin in self.plugins.values()

        ]