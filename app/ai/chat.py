"""
Chat Module
"""
from langchain.agents import OpenAIFunctionsAgent
from langchain.prompts import (PromptTemplate, ChatPromptTemplate,
                               HumanMessagePromptTemplate, MessagesPlaceholder)
from langchain.schema import SystemMessage

from app.ai.chains import StreamingAgentExecutor
from app.ai.llms import build_llm
from app.ai.memories import build_memory
from app.config import CUSTOM_PROMPT_TEMPLATE, CUSTOM_PROMPT
from app.models.chat import ChatArgs
from .handlers import build_token_handler
from .tools import token_usage_tool, vector_tool

PROMPT = PromptTemplate(
            template=CUSTOM_PROMPT_TEMPLATE,
            input_variables=["name", "question", "context",
                         "chat_history"]
        )
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=(CUSTOM_PROMPT)),
        MessagesPlaceholder(variable_name="chat_history"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

def build_agent(chat_args: ChatArgs):
    token_handler = build_token_handler(chat_args)
    handlers = [token_handler]
    llm = build_llm(chat_args, handlers)
    memory = build_memory(chat_args)
    tools = [token_usage_tool, vector_tool]
    agent = OpenAIFunctionsAgent(
        llm=llm,
        prompt=prompt,
        tools=tools
    )
    return StreamingAgentExecutor(
        agent=agent,
        verbose=True,
        tools=tools,
        memory=memory
    )