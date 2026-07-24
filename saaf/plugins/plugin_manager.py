from saaf.plugins.plugin_registry import PluginRegistry
from saaf.tools.plugin_loader import PluginLoader
from saaf.plugins.capability_router import CapabilityRouter
from saaf.plugins.plugin_discoverer import PluginDiscoverer



class PluginManager:
    """
    Manages plugin loading and discovery.
    """


    def __init__(self):

        self.registry = PluginRegistry()
        self.loader = PluginLoader()
        self.discoverer = PluginDiscoverer()
        self.router = CapabilityRouter(self.registry)



    def load_plugins(self):

        plugins = self.discoverer.discover()
        for plugin in plugins:
            self.registry.register(
                plugin
            )
        return plugins

    def get_registry(self):
        return self.registry
    
    def list_plugins(self):
        return [
            {
                "name": plugin.metadata.name,
                "version": plugin.metadata.version,
                "capabilities": plugin.metadata.capabilities,
                "priority": plugin.metadata.priority
            }
            for plugin in self.registry.plugins
        ]