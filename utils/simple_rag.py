import os
from pathlib import Path
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

def load_all_python_files(root_dir: str = ".") -> str:

    code_blocks = []
    root_path = Path(root_dir).resolve()

    skip_folders = { "venv", "__pycache__", ".git", "chroma_db", "reports"}

    for py_file in sorted(root_path.rglob("*.py")):
        # Skip files inside skip_folders
        if any(skip in str(py_file) for skip in skip_folders):
            continue
            
        try:
            content = py_file.read_text(encoding="utf-8")
            relative_path = py_file.relative_to(root_path)
            
            code_blocks.append(
                f"=== FILE: {relative_path} ===\n{content}\n"
            )
        except Exception as e:
            print(f"Skipping {py_file}: {e}")
    
    return "\n".join(code_blocks)


def ask_ai_about_codebase(question: str, root_dir: str = ".") -> str:
    """
    Loads all Python files and asks Ollama a question about them.
    """
    print("Reading your codebase...")
    codebase = load_all_python_files(root_dir)
    
    # Truncate if massive (local models have limited context)
    max_chars = 70000  # adjust based on your model's limit
    if len(codebase) > max_chars:
        print(f"Codebase is large ({len(codebase)} chars). Truncating to {max_chars}.")
        codebase = codebase[:max_chars] + "\n... [truncated]"
    
    prompt = f"""You are reviewing a Python Appium test automation project.
    Below are all the Python files in the project.

    {codebase}

    ---
    Question: {question}

    Answer based only on the code above. Be specific about file names and line numbers."""

    print("Asking Ollama...")
    llm = ChatOllama(
        model="minimax-m3:cloud",
        base_url="http://localhost:11434"
    )
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return getattr(response, "content", str(response))


if __name__ == "__main__":
    question = input("What do you want to know about your codebase?\n> ")
    answer = ask_ai_about_codebase(question)
    print("\n" + "="*50)
    print(answer)