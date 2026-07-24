from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowState:
    """
    Shared state between workflow nodes.
    """

    user_id: str

    request: str


    data: dict[str, Any] = field(
        default_factory=dict
    )


    results: list[Any] = field(
        default_factory=list
    )


    status: str = "created"



    def set(
        self,
        key,
        value
    ):

        self.data[key] = value



    def get(
        self,
        key
    ):

        return self.data.get(key)



    def add_result(
        self,
        result
    ):

        self.results.append(
            result
        )
    
    def update(self, values: dict):

        self.data.update(values)



    def has(self, key):

        return key in self.data



    def clear(self):

        self.data.clear()
        self.results.clear()    