from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionContext:

    user_id: str

    request: str

    status: str = "initialized"

    results: list[Any] = field(
        default_factory=list
    )

    variables: dict[str, Any] = field(
        default_factory=dict
    )    
    
    def add_result(self, result):

        self.results.append(
            result
        )


    def set_variable(
        self,
        key,
        value
    ):

        self.variables[key] = value


    def get_variable(
        self,
        key
    ):

        return self.variables.get(
            key
        )