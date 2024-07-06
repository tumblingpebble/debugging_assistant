from typing import Any, Dict, List, Optional, Union
from uuid import UUID
from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.generations import GenerationChunk, ChatGenerationChunk, LLMResult
from langchain_core.documents import Document
from langchain_core.retries import RetryCallState
from callbacks.base import BaseCallbackHandler

class FileCallbackHandler(BaseCallbackHandler):
    def __init__(self, filename: str, mode: str = 'a', color: Optional[str] = None) -> None:
        self.filename = filename
        self.mode = mode
        self.color = color

    def _write_to_file(self, text: str) -> None:
        with open(self.filename, self.mode) as f:
            f.write(text + "\n")

    def on_agent_action(self, action: AgentAction, color: Optional[str] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"Agent Action: {action}")
        return None

    def on_agent_finish(self, finish: AgentFinish, color: Optional[str] = None, **kwargs: Any) -> None:
        self._write_to_file(f"Agent Finish: {finish}")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        self._write_to_file(f"Chain End: {outputs}")

    def on_chain_error(self, error: BaseException, *, run_id: UUID, parent_run_id: Optional[UUID] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"Chain Error: {error}")
        return None

    def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any) -> None:
        self._write_to_file(f"Chain Start: {serialized}, Inputs: {inputs}")

    def on_chat_model_start(self, serialized: Dict[str, Any], messages: List[List['BaseMessage']], *, run_id: UUID, parent_run_id: Optional[UUID] = None, tags: Optional[List[str]] = None, metadata: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"Chat Model Start: {serialized}, Messages: {messages}")
        return None

    def on_llm_end(self, response: LLMResult, *, run_id: UUID, parent_run_id: Optional[UUID] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"LLM End: {response}")
        return None

    def on_llm_error(self, error: BaseException, *, run_id: UUID, parent_run_id: Optional[UUID] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"LLM Error: {error}")
        return None

    def on_llm_new_token(self, token: str, *, chunk: Optional[Union[GenerationChunk, ChatGenerationChunk]] = None, run_id: UUID, parent_run_id: Optional[UUID] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"LLM New Token: {token}")
        return None

    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], *, run_id: UUID, parent_run_id: Optional[UUID] = None, tags: Optional[List[str]] = None, metadata: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"LLM Start: {serialized}, Prompts: {prompts}")
        return None

    def on_retriever_end(self, documents: Sequence[Document], *, run_id: UUID, parent_run_id: Optional[UUID] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"Retriever End: {documents}")
        return None

    def on_retriever_error(self, error: BaseException, *, run_id: UUID, parent_run_id: Optional[UUID] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"Retriever Error: {error}")
        return None

    def on_retriever_start(self, serialized: Dict[str, Any], query: str, *, run_id: UUID, parent_run_id: Optional[UUID] = None, tags: Optional[List[str]] = None, metadata: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"Retriever Start: {serialized}, Query: {query}")
        return None

    def on_retry(self, retry_state: RetryCallState, *, run_id: UUID, parent_run_id: Optional[UUID] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"Retry: {retry_state}")
        return None

    def on_text(self, text: str, color: Optional[str] = None, end: str = '', **kwargs: Any) -> None:
        self._write_to_file(f"Text: {text}")

    def on_tool_end(self, output: str, color: Optional[str] = None, observation_prefix: Optional[str] = None, llm_prefix: Optional[str] = None, **kwargs: Any) -> None:
        self._write_to_file(f"Tool End: {output}")

    def on_tool_error(self, error: BaseException, *, run_id: UUID, parent_run_id: Optional[UUID] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"Tool Error: {error}")
        return None

    def on_tool_start(self, serialized: Dict[str, Any], input_str: str, *, run_id: UUID, parent_run_id: Optional[UUID] = None, tags: Optional[List[str]] = None, metadata: Optional[Dict[str, Any]] = None, inputs: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        self._write_to_file(f"Tool Start: {serialized}, Input: {input_str}")
        return None
