from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
import os
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage 

class POMCodebaseRAG:

    def __init__(self, pages_dir: str = "pages", model:str = "minimax-m3:cloud"):

        self.pages_dir = pages_dir
        self.model = model
        self.vectorstore = None
        self.retriever = None

        self._load_documents()
        self._split_documents()
        self._store_vectors()

    def _load_documents(self):
        loader = DirectoryLoader(
            path = self.pages_dir,
            glob = "**/*.py",
            show_progress=True
        )
        self.documents = loader.load()

    def _split_documents(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 100,
            separators=["\nclass ", "\ndef ", "\n\n", "\n", " ", ""]
        )
        self.chunks = text_splitter.split_documents(self.documents)


    def _store_vectors(self):
        embeddings = OllamaEmbeddings(
            model = self.model,
            base_url = "http://localhost:11434"
        )

        self.vectorstore = Chroma.from_documents(
            documents = self.chunks,
            embedding = embeddings,
            persist_directory = "./chroma_db"
        )

        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})
        print("Vector store created and ready.")

    def ask_with_context(self, question: str) -> str:
        """
        Retrieves relevant code chunks, then asks the LLM with that context.
        """
        # RETRIEVE — find the 3 most relevant chunks
        relevant_chunks = self.retriever.invoke(question) # type: ignore
        
        # Build context string from retrieved code
        context = "\n\n---\n\n".join([
            f"File: {doc.metadata.get('source', 'unknown')}\n{doc.page_content}"
            for doc in relevant_chunks
        ])
        
        # AUGMENT — build the prompt with context + question
        prompt = f"""You are a senior mobile test automation engineer.
                Below are relevant code snippets from the test codebase.

        {context}   

        Based on the code above, answer this question:
        {question}

        Be specific. Reference file names and line numbers if possible."""

        # GENERATE — send to Ollama
        llm = ChatOllama(model=self.model, base_url="http://localhost:11434")
        response = llm.invoke([HumanMessage(content=prompt)])
        
        return getattr(response, "content", str(response))

    def find_similar_code(self, query:str ):
        return self.retriever.invoke(query) # type: ignore


_rag_instance = None
def get_rag():
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = POMCodebaseRAG()
    return _rag_instance