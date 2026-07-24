from dataclasses import dataclass, field
from typing import List


@dataclass
class PluginMetadata:
    """
    Metadata describing an SAAF plugin.

    Used by the agent to understand:
    - plugin identity
    - capabilities
    - execution properties
    """


    name: str

    version: str

    description: str

    category: str


    capabilities: List[str] = field(
        default_factory=list
    )


    priority: int = 0


    cost: str = "free"


    requires_network: bool = False


    supports_async: bool = False


    supports_streaming: bool = False