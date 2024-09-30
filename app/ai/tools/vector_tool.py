from langchain.agents import Tool

from app.ai.vectors import build_vector_store


def vector_tool_query(query):
    vectorstore = build_vector_store()
    results = vectorstore.similarity_search(query)
    return results

vector_tool = Tool(
    name="VectorQueryTool",
    func=vector_tool_query,
    description="Use this tool when query contains details about spices. Pass the query to the tool."
)