from saaf.response.formatters.base_formatter import BaseFormatter

class WeatherFormatter(BaseFormatter):
    """
    Formats weather tool responses.
    """
    @property
    def tool_name(self):
        return 'weather'
    
    def format(self,result):
        weather = result['output']        
        return (
            f"Weather in {weather['city']}:\n"
            f"Temperature: {weather['temperature']}\n"
            f"Condition: {weather['condition']}"
        )

formatter = WeatherFormatter()