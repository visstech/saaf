from dataclasses import dataclass, field
from typing import Optional, List, Dict



@dataclass
class AgentStep:
    """
    Single workflow step.
    """

    action: str

    tool: Optional[str] = None

    input: Optional[str] = None

    memory_key: Optional[str] = None



@dataclass
class AgentIntent:
    """
    Standard SAAF agent intent.

    Every LLM response becomes this object.
    """

    action: str
    tool: Optional[str] = None
    capability: str = None
    input: Optional[str] = None
    memory_key: Optional[str] = None
    steps: List[AgentStep] = field(
                default_factory=list
            )
    raw: Dict = field(
        default_factory=dict
    )