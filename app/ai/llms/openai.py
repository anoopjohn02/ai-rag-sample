"""
OpenAI Module
"""
import tiktoken
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from app.models.chat import ChatArgs
from app.models.token import TransactionalTokens
from app.config import OpenaiConfig as config
from app.ai.handlers import TokenAsyncHandler

OPENAI_EMBEDDING_MODEL = "text-embedding-ada-002"
embeddings = OpenAIEmbeddings(model = OPENAI_EMBEDDING_MODEL)
encoding = tiktoken.encoding_for_model(OPENAI_EMBEDDING_MODEL)

def build_openai_llm(chat_args: ChatArgs):
    """
    Build OpenAI Model
    Args:
        chat_args(ChatArgs): Arguments needed for building OpenAI model
    """
    model_name = config.model
    token = TransactionalTokens(query=chat_args.query,
                                transaction_id=chat_args.transaction_id,
                                conversation_id=chat_args.conversation_id,
                                model=model_name,
                                embedding_model=OPENAI_EMBEDDING_MODEL)
    return ChatOpenAI(
        streaming=chat_args.streaming,
        model_name=model_name,
        callbacks=[TokenAsyncHandler(token, calculate_openai_tokens)],
    )

def build_openai_condense_llm():
    """
    Build condense OpenAI model
    """
    return ChatOpenAI(streaming=False)

def calculate_openai_tokens(texts):
    """
    Calculate tokens in a text
    """
    total_tokens = sum(len(encoding.encode(text))
                       for text in texts)
    return total_tokens
