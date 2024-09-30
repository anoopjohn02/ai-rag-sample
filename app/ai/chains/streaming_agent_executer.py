"""
Streaming Conversational Retrieval Chain
"""
from langchain.agents import AgentExecutor
from app.ai.chains.stream import Streamable

class StreamingAgentExecutor(Streamable, AgentExecutor):
    """
    Custom class for streaming
    """
    def __init__(self, handler, agent, verbose, tools, memory):
        AgentExecutor.__init__(self, agent=agent, verbose=verbose, tools=tools, memory=memory)
        self.set_handler(handler)
