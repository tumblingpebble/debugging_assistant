from typing import List
from langchain_core.runnables import RunnableConfig, Runnable

async def aconfig_with_context(config: RunnableConfig, steps: List[Runnable]) -> RunnableConfig:
    # Implementation to asynchronously patch a runnable config with context getters and setters
    ...

def config_with_context(config: RunnableConfig, steps: List[Runnable]) -> RunnableConfig:
    # Implementation to patch a runnable config with context getters and setters
    ...
