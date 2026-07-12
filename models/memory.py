from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Memory:
    """
    Represents a memory in SAAF.

    This is a business/domain object.
    It contains only memory-related information.

    Database-specific fields such as:
    - id
    - created_at
    - updated_at

    are managed by the storage layer.
    """

    user_id: str
    memory_key: str
    memory_value: Any
    memory_type: str
    importance: int = 1