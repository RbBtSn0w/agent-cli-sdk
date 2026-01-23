from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Union
from enum import Enum

class Role(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"

@dataclass
class Message:
    role: Role
    content: str
    name: Optional[str] = None
    tool_calls: Optional[List[Dict[str, Any]]] = None

@dataclass
class ToolDefinition:
    name: str
    description: str
    parameters: Dict[str, Any]  # JSON Schema
    function: callable = field(repr=False)

class AgentEvent(Enum):
    START = "start"
    THOUGHT = "thought"
    TOOL_CALL = "tool_call"
    TOOL_RESULT = "tool_result"
    CONTENT = "content"
    DONE = "done"
    ERROR = "error"

@dataclass
class StreamEvent:
    type: AgentEvent
    payload: Any
