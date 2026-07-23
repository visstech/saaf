import importlib
import os


class PluginDiscoverer:
    """
    Automatically discovers plugins
    from plugin directories.
    """


    def __init__(
        self,
        plugin_path="saaf.tools.plugins"
    ):

        self.plugin_path = plugin_path



    def discover(self):

        plugins = []


        package_path = (
            self.plugin_path.replace(
                ".",
                "/"
            )
        )


        if not os.path.exists(
            package_path
        ):

            return plugins



        for folder in os.listdir(
            package_path
        ):

            full_path = os.path.join(
                package_path,
                folder
            )


            if not os.path.isdir(
                full_path
            ):

                continue


            try:

                module = importlib.import_module(
                    f"{self.plugin_path}.{folder}"
                )


                if hasattr(
                    module,
                    "tool"
                ):

                    plugins.append(
                        module.tool
                    )


                    print(
                        "[Plugin Discovery]",
                        folder
                    )


            except Exception as e:

                print(
                    "[Plugin Discovery Failed]",
                    folder,
                    e
                )


        return plugins