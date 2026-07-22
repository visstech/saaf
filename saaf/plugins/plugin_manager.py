from saaf.plugins.plugin_registry import PluginRegistry
from saaf.tools.plugin_loader import PluginLoader



class PluginManager:
    """
    Manages plugin loading and discovery.
    """


    def __init__(self):

        self.registry = PluginRegistry()

        self.loader = PluginLoader()



    def load_plugins(self):

        plugins = self.loader.load_plugins()


        for plugin in plugins:

            self.registry.register(
                plugin
            )


        return plugins



    def get_registry(self):

        return self.registry