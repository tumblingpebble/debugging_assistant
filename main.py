from agent_environment import env
from agent_actions import AgentAction
from context.context import Context
from callbacks.file_handler import FileCallbackHandler
from callbacks.manager import BaseCallbackManager, handle_event, ahandle_event, trace_as_chain_group
from chat_history.in_memory import InMemoryChatMessageHistory
from caches.in_memory import InMemoryCache
from typing import Union

def create_and_execute_action(tool: str, tool_input: Union[str, dict], log: str):
    action = AgentAction(log=log, tool=tool, tool_input=tool_input)
    step = env.execute_action(action)
    return step

def finalize_agent(return_values: dict):
    finish = env.finish(return_values)
    return finish

if __name__ == "__main__":
    # Create context scope
    context_scope = Context.create_scope("debugging")

    # Set initial context
    context_setter = context_scope.setter("initial_context", "Initial context value")
    context_setter.invoke(None)

    # Setup callback manager
    file_handler = FileCallbackHandler(filename="log.txt")
    callback_manager = BaseCallbackManager(handlers=[file_handler])

    # Create chat message history
    chat_history = InMemoryChatMessageHistory()

    # Add initial messages to chat history
    chat_history.add_user_message("Hello, how can I assist you?")
    chat_history.add_ai_message("I need help with debugging.")

    # Retrieve and print chat messages
    for message in chat_history.messages:
        print(f"{message.sender}: {message.content}")

    # Create and execute an action
    step = create_and_execute_action(tool="Debugger", tool_input={"code": "print('Hello, World!')"}, log="Initial debugging")
    print(step.observation)

    # Retrieve context value
    context_getter = context_scope.getter("initial_context")
    context_value = context_getter.invoke(None)
    print(f"Retrieved context: {context_value}")

    # Log the step
    handle_event(callback_manager.handlers, "on_tool_end", None, step.observation)

    # Finalize the agent's process
    final_result = finalize_agent(return_values={"result": "Success"})
    print(final_result.log)
    print(final_result.return_values)

    # Log the final result
    handle_event(callback_manager.handlers, "on_agent_finish", None, final_result)

    # Setup cache
    cache = InMemoryCache()

    # Use cache
    prompt = "What is the capital of France?"
    llm_string = "model=v1"
    cached_result = cache.lookup(prompt, llm_string)
    if cached_result is None:
        # Simulate LLM call
        result = [{"text": "The capital of France is Paris."}]
        cache.update(prompt, llm_string, result)
    else:
        print(f"Cache hit: {cached_result}")

    # Example of using trace_as_chain_group
    llm_input = "Foo"
    with trace_as_chain_group("group_name", callback_manager=callback_manager, inputs={"input": llm_input}) as manager:
        res = env.invoke(llm_input, {"callbacks": manager})
        manager.on_chain_end({"output": res})
