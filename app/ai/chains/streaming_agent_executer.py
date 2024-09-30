"""
Streaming Conversational Retrieval Chain
"""
from typing import Any
from langchain.agents import AgentExecutor
from app.ai.chains.stream import Streamable
from app.ai.handlers import StreamingHandler


class StreamingAgentExecutor(Streamable, AgentExecutor):
    """
    Custom class for streaming
    """
    pass