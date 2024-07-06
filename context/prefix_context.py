from typing import Union, List, Optional, Callable, Awaitable
from context.context_get import ContextGet
from context.context_set import ContextSet

class PrefixContext:
    def __init__(self, prefix: str = ''):
        self.prefix = prefix

    def getter(self, key: Union[str, List[str]]) -> ContextGet:
        return ContextGet(key=key)

    def setter(
        self,
        _key: Optional[str] = None,
        _value: Optional[Union[Callable, Awaitable, any]] = None,
        **kwargs: Union[Callable, Awaitable, any]
    ) -> ContextSet:
        return ContextSet(keys={_key: _value, **kwargs})
