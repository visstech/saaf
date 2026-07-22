from typing import Dict

from saaf.plugins.base_plugin import BasePlugin



class PluginRegistry:
    """
    Stores SAAF plugins
    and provides plugin intelligence.
    """


    def __init__(self):

        self.plugins: Dict[str, BasePlugin] = {}



    def register(
        self,
        plugin: BasePlugin
    ):

        name = plugin.metadata.name


        self.plugins[name] = plugin



    def get(
        self,
        name: str
    ):

        return self.plugins.get(
            name
        )



    def list_plugins(
        self
    ):

        return list(
            self.plugins.values()
        )

    def find_by_capability(
        self,
        capability: str
    ):

        matches = []


        for plugin in self.plugins.values():

            if capability in plugin.metadata.capabilities:

                matches.append(
                    plugin
                )


        return matches

    def metadata(
        self
    ):

        return [

            plugin.metadata

            for plugin in self.plugins.values()

        ]