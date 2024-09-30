import logging
from langchain.agents import Tool
import logging

from langchain.agents import Tool


def token_usage_query(query):
    logging.log("token_usage_query: User with id ")
    return []

token_usage_tool = Tool(
    name="SQLQueryTool",
    func=token_usage_query,
    description="Use this tool when query contains token usages, costs, transactions, conversations etc...",
    #args_schema={"type": "object", "properties": {"query": {"type": "string"}, "chat_args": {"type": "string"}}}
)