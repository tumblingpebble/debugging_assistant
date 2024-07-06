from typing import Union, List, Optional, Callable, Awaitable
from context.context_get import ContextGet
from context.context_set import ContextSet
from context.prefix_context import PrefixContext

class Context:
    @staticmethod
    def create_scope(scope: str) -> PrefixContext:
        return PrefixContext(prefix=scope)

    @staticmethod
    def getter(key: Union[str, List[str]]) -> ContextGet:
        return ContextGet(key=key)

    @staticmethod
    def setter(
        _key: Optional[str] = None,
        _value: Optional[Union[Callable, Awaitable, any]] = None,
        **kwargs: Union[Callable, Awaitable, any]
    ) -> ContextSet:
        return ContextSet(keys={_key: _value, **kwargs})
