"""
Streaming Conversational Retrieval Chain
"""
from langchain.chains import ConversationalRetrievalChain
from app.ai.chains.stream import StreamableChain

class StreamingConversationalRetrievalChain(StreamableChain, ConversationalRetrievalChain):
    """
    Custom class for streaming
    """
    pass
