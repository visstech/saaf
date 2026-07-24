import importlib
import pkgutil

import saaf.response.formatters as formatters


class FormatterLoader:
    """
    Dynamically loads all formatter plugins.
    """

    def load_formatters(self):

        loaded = []

        for _, module_name, _ in pkgutil.iter_modules(
            formatters.__path__
        ):

            if module_name == "base_formatter":
                continue

            module = importlib.import_module(
                f"saaf.response.formatters.{module_name}"
            )

            if hasattr(module, "formatter"):

                loaded.append(
                    module.formatter
                )

        return loaded