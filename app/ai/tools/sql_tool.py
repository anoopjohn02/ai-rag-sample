
import uuid
import logging

from langchain.agents import Tool
from app.services import get_user_message_token_usage

def token_usage_query(query):
    logging.log("token_usage_query: User with id ")
    return get_user_message_token_usage(uuid.UUID(user_id).hex)

token_usage_tool = Tool(
    name="SQLQueryTool",
    func=token_usage_query,
    description="Use this tool when query contains token usages, costs, transactions, conversations etc...",
    #args_schema={"type": "object", "properties": {"query": {"type": "string"}, "chat_args": {"type": "string"}}}
)