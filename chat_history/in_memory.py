from typing import List, Sequence, Union
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage
from chat_history.base import BaseChatMessageHistory

class InMemoryChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, messages: List[BaseMessage] = None):
        self._messages = messages or []

    @property
    def messages(self) -> List[BaseMessage]:
        return self._messages

    def add_message(self, message: BaseMessage) -> None:
        self._messages.append(message)

    def clear(self) -> None:
        self._messages = []

    async def aadd_messages(self, messages: Sequence[BaseMessage]) -> None:
        self.add_messages(messages)

    async def aclear(self) -> None:
        self.clear()
