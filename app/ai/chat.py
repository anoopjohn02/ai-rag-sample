"""
Chat Module
"""
from langchain.prompts import (PromptTemplate, ChatPromptTemplate,
                               HumanMessagePromptTemplate,MessagesPlaceholder)
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from langchain.schema import SystemMessage
from app.ai.chains import StreamingConversationalRetrievalChain, StreamingAgentExecutor
from app.ai.llms import build_llm, build_condense_llm
from app.ai.vectors import build_retriever
from app.ai.memories import build_memory
from app.models.chat import ChatArgs
from .handlers import build_token_handler, build_streaming_handler
from .tools import token_usage_tool, vector_tool
from app.config import CUSTOM_PROMPT_TEMPLATE, CUSTOM_PROMPT

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
def build_chain(chat_args: ChatArgs):
    """
    Build chat for given arguiments
    """
    #llm = build_llm(chat_args)
    #retriever = build_retriever()
    #memory = build_memory(chat_args)
    #condense_llm = build_condense_llm()
    #return StreamingConversationalRetrievalChain.from_llm(
    #    llm = llm,
    #    condense_question_llm = condense_llm,
    #    memory = memory,
    #    retriever = retriever,
    #    combine_docs_chain_kwargs={"prompt": PROMPT},
    #    return_source_documents=True,
    #    return_generated_question=True
    #)
    return None

def build_agent(chat_args: ChatArgs):
    token_handler = build_token_handler(chat_args)
    streaming_handler = build_streaming_handler()
    handlers = [token_handler, streaming_handler]
    llm = build_llm(chat_args, handlers)
    memory = build_memory(chat_args)
    tools = [token_usage_tool, vector_tool]
    agent = OpenAIFunctionsAgent(
        llm=llm,
        prompt=prompt,
        tools=tools
    )
    return StreamingAgentExecutor(
        handler=streaming_handler,
        agent=agent,
        verbose=True,
        tools=tools,
        memory=memory,
    )