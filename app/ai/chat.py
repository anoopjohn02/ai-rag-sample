"""
Chat Module
"""
from langchain.prompts import PromptTemplate
from app.ai.chains import StreamingConversationalRetrievalChain
from app.ai.llms import build_llm, build_condense_llm
from app.ai.vectors import build_retriever
from app.ai.memories import build_memory
from app.models.chat import ChatArgs
from app.config import CUSTOM_PROMPT_TEMPLATE

PROMPT = PromptTemplate(
            template=CUSTOM_PROMPT_TEMPLATE,
            input_variables=["name", "question", "context",
                         "chat_history"]
        )
def build_chat(chat_args: ChatArgs):
    """
    Build chat for given arguiments
    """
    llm = build_llm(chat_args)
    retriever = build_retriever()
    memory = build_memory(chat_args)
    condense_llm = build_condense_llm()
    return StreamingConversationalRetrievalChain.from_llm(
        llm = llm,
        condense_question_llm = condense_llm,
        memory = memory,
        retriever = retriever,
        combine_docs_chain_kwargs={"prompt": PROMPT},
        return_source_documents=True,
        return_generated_question=True
    )
