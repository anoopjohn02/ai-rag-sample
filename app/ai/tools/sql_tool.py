
import uuid
import logging

from langchain_core.tools import tool, InjectedToolArg, Tool
from typing_extensions import Annotated

from app.models.token import TokenUsage
from app.services.token_usage import get_user_message_token_usage

def token_usage_tool(user_id: str) -> TokenUsage:
    logging.info("token_usage_query: User with id %s", user_id)
    return get_user_message_token_usage(uuid.UUID(user_id).hex)

def define_user_token_usage_tool(user_id: str):
    return Tool.from_function(
        name="token_usage_tool",
        description=f"Use this tool when query contains token usages, costs, transactions, and conversations. "
                    f"Pass user_id = {user_id} to the tool",
        func=token_usage_tool
    )