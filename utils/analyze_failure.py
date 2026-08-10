# utils/analyze_failure.py
import sys
from simple_rag import ask_ai_about_codebase

error_log = sys.argv[1] if len(sys.argv) > 1 else "Unknown error"

question = f"""A test failed with this error:
{error_log}

Look at the codebase. What is the root cause? Which file should I fix?"""

print(ask_ai_about_codebase(question))