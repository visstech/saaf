from saaf.tools.base_tool import BaseTool
from saaf.plugins.base_plugin import BasePlugin
from saaf.plugins.metadata import PluginMetadata


class WeatherTool(BaseTool,BasePlugin):
    """
    Weather information tool.

    Currently a mock implementation.
    Later we can connect real weather APIs.
    """


    name = "weather"


    description = (
        "Provides weather information "
        "for a given city."
    )


    version = "1.0"


    category = "information"



    @property
    def schema(self):

        return {

            "name": self.name,

            "description": self.description,

            "version": self.version,

            "category": self.category,

            "parameters": {

                "city":
                "City name"

            },

            "examples": [

                "weather in Kuala Lumpur",

                "temperature in London",

                "weather forecast for Chennai"

            ]

        }

    @property
    def metadata(self):
    
            return PluginMetadata(
    
                name="weather",
    
                version="1.0",
    
                description=(
                    "Provides weather information "
                    "for a given city."
                ),
    
                category="information",
    
                capabilities=[
    
                    "weather",
    
                    "temperature",
    
                    "forecast"
    
                ],
    
                priority=8,
    
                cost="free",
    
                requires_network=True,
    
                supports_async=False,
    
                supports_streaming=False
    
            )    
            

    def execute(
        self,
        query: str
    ):

        if not query:
            return {
                "tool": self.name,
                "error": "No city provided."
            }

        city = query.strip()


        # Mock response

        return {

            "tool": self.name,

            "input": city,

            "output": {

                "city": city,

                "temperature": "32°C",

                "condition": "Sunny"

            }

        }
    