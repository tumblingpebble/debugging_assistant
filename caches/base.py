from abc import ABC, abstractmethod
from typing import Any, Optional, Sequence
from langchain_core.generations import Generation

class BaseCache(ABC):
    @abstractmethod
    def lookup(self, prompt: str, llm_string: str) -> Optional[Sequence[Generation]]:
        pass

    @abstractmethod
    def update(self, prompt: str, llm_string: str, return_val: Sequence[Generation]) -> None:
        pass

    @abstractmethod
    def clear(self, **kwargs: Any) -> None:
        pass

    async def aclear(self, **kwargs: Any) -> None:
        self.clear(**kwargs)

    async def alookup(self, prompt: str, llm_string: str) -> Optional[Sequence[Generation]]:
        return self.lookup(prompt, llm_string)

    async def aupdate(self, prompt: str, llm_string: str, return_val: Sequence[Generation]) -> None:
        self.update(prompt, llm_string, return_val)
