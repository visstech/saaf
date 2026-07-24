
from saaf.response.formatters.base_formatter import BaseFormatter

class CalculatorFormatter(BaseFormatter):
    """
    Formats calculator tool responses.
    """
    @property
    def tool_name(self):
        return 'calculator'
    
    def format(self,result):
        value = result['output']
        if isinstance(value,float):
            value = round(value,4)
            
        return (f'The result of ' 
                f'{result['input']}'
                f' is {value}.' )

formatter = CalculatorFormatter()