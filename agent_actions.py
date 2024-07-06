from typing import Union, Sequence
from pydantic import BaseModel, ValidationError
from pydantic.types import Literal
from utils.message import BaseMessage

class AgentAction(BaseModel):
    log: str
    tool: str
    tool_input: Union[str, dict]
    type: Literal['AgentAction'] = 'AgentAction'

    @property
    def messages(self) -> Sequence[BaseMessage]:
        return []

class AgentActionMessageLog(AgentAction):
    message_log: Sequence[BaseMessage]
    type: Literal['AgentActionMessageLog'] = 'AgentActionMessageLog'

    @property
    def messages(self) -> Sequence[BaseMessage]:
        return self.message_log

class AgentFinish(BaseModel):
    log: str
    return_values: dict
    type: Literal['AgentFinish'] = 'AgentFinish'

    @property
    def messages(self) -> Sequence[BaseMessage]:
        return []

class AgentStep(BaseModel):
    action: AgentAction
    observation: Union[str, None] = None

    @property
    def messages(self) -> Sequence[BaseMessage]:
        return []
