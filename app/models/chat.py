"""
Chat Module contains chat models
"""
import uuid

from pydantic import BaseModel


class Request(BaseModel):
    """
    Chat request from client
    """
    question: str
    new_chat: bool

class Response(BaseModel):
    """
    Chat response
    """
    text: str

class ChatArgs():
    """
    Chat arguments
    """
    query: str
    conversation_id: uuid
    transaction_id: uuid
    streaming: bool

    def __init__(self, query, conversation_id, transaction_id, streaming):
        self.query = query
        self.conversation_id = conversation_id
        self.transaction_id = transaction_id
        self.streaming = streaming
