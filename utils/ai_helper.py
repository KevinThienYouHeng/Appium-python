from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from utils.codebase_rag import get_rag

# def ask_ai_to_analyze_failure(error_log: str) -> str:
#     """
#     Sends the pytest failure traceback to a local Ollama model for analysis.
#     """
#     try:
#         llm = ChatOllama(
#             model="minimax-m3:cloud",
#             base_url="http://localhost:11434",
#         )
        
#         prompt = (
#             "You are a mobile test automation expert. "
#             "An Appium Python test failed. Explain the root cause "
#             "and suggest how to fix the test script.\n\n"
#             f"Error log:\n{error_log[:3000]}"  # truncate if huge
#         )
        
#         response = llm.invoke([HumanMessage(content=prompt)])
        
#         # Safe access to avoid type checker complaints
#         return getattr(response, "content", str(response))
        
#     except Exception as e:
#         return f"AI analysis unavailable: {e}"

def ask_ai_to_analyze_failure(error_log: str) -> str:
    """
    Sends the failure + relevant codebase context to the LLM.
    """
    try:
        rag = get_rag()  # loads POM files once, reuses after
        
        question = (
            f"A test failed with this error:\n\n{error_log[:2000]}\n\n"
            "What is the root cause? Which POM method is likely broken? "
            "How should I fix it?"
        )
        
        return rag.ask_with_context(question)
        
    except Exception as e:
        return f"AI analysis unavailable: {e}"