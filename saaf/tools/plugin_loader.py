import importlib
import pkgutil

import saaf.tools.plugins as plugins



class PluginLoader:
    """
    Automatically discovers SAAF tool plugins.
    """



    def load_plugins(self):

        loaded_tools = []


        for module in pkgutil.iter_modules(
            plugins.__path__
        ):

            package_name = (
                "saaf.tools.plugins."
                + module.name
            )


            module = importlib.import_module(
                package_name
            )


            if hasattr(
                module,
                "tool"
            ):

                loaded_tools.append(
                    module.tool
                )


        return loaded_tools