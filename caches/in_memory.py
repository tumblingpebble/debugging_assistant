from typing import Any, Optional, Sequence, Dict
from langchain_core.generations import Generation
from caches.base import BaseCache

class InMemoryCache(BaseCache):
    def __init__(self):
        self.cache: Dict[str, Sequence[Generation]] = {}

    def _generate_key(self, prompt: str, llm_string: str) -> str:
        return f"{prompt}:{llm_string}"

    def lookup(self, prompt: str, llm_string: str) -> Optional[Sequence[Generation]]:
        key = self._generate_key(prompt, llm_string)
        return self.cache.get(key)

    def update(self, prompt: str, llm_string: str, return_val: Sequence[Generation]) -> None:
        key = self._generate_key(prompt, llm_string)
        self.cache[key] = return_val

    def clear(self, **kwargs: Any) -> None:
        self.cache.clear()

    async def aclear(self, **kwargs: Any) -> None:
        self.clear(**kwargs)

    async def alookup(self, prompt: str, llm_string: str) -> Optional[Sequence[Generation]]:
        return self.lookup(prompt, llm_string)

    async def aupdate(self, prompt: str, llm_string: str, return_val: Sequence[Generation]) -> None:
        self.update(prompt, llm_string, return_val)
