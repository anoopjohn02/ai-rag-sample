from langchain.agents import Tool

from app.ai.vectors import build_vector_store
from langchain_core.tools import tool

@tool
def vector_tool(query):
    """
    Use this tool when query contains details about spices. Pass the query to the tool.
    """
    vectorstore = build_vector_store()
    results = vectorstore.similarity_search(query)
    return results
