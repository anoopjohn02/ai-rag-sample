
import uuid
import logging

from langchain_core.tools import tool, InjectedToolArg
from typing_extensions import Annotated

from app.models.token import TokenUsage
from app.services.token_usage import get_user_message_token_usage

@tool(parse_docstring=True)
def token_usage_tool(user_id: Annotated[str, InjectedToolArg]) -> TokenUsage:
    """
    Use this tool when query contains token usages, costs, transactions, and conversations.

    Args:
        user_id: User's ID.

    Returns:
        The return value. List of user token usages.
    """
    logging.info("token_usage_query: User with id %s", user_id)
    return get_user_message_token_usage(uuid.UUID(user_id).hex)
