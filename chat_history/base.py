from abc import ABC, abstractmethod
from typing import List, Sequence, Union
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage

class BaseChatMessageHistory(ABC):
    @property
    @abstractmethod
    def messages(self) -> List[BaseMessage]:
        pass

    @abstractmethod
    def add_message(self, message: BaseMessage) -> None:
        pass

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        for message in messages:
            self.add_message(message)

    async def aadd_messages(self, messages: Sequence[BaseMessage]) -> None:
        self.add_messages(messages)

    @abstractmethod
    def clear(self) -> None:
        pass

    async def aclear(self) -> None:
        self.clear()

    def add_ai_message(self, message: Union[AIMessage, str]) -> None:
        self.add_message(AIMessage(content=message) if isinstance(message, str) else message)

    def add_user_message(self, message: Union[HumanMessage, str]) -> None:
        self.add_message(HumanMessage(content=message) if isinstance(message, str) else message)

    async def aget_messages(self) -> List[BaseMessage]:
        return self.messages
