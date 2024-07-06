from typing import Any, List, Optional
from callbacks.base import BaseCallbackHandler

async def ahandle_event(handlers: List[BaseCallbackHandler], event_name: str, ignore_condition_name: Optional[str], *args: Any, **kwargs: Any) -> None:
    for handler in handlers:
        if ignore_condition_name and getattr(handler, ignore_condition_name, False):
            continue
        event_method = getattr(handler, event_name, None)
        if event_method:
            await event_method(*args, **kwargs)
