import os
from llama_index import SimpleDirectoryReader
from llama_index import GPTSimpleVectorIndex
os.environ['OPENAI_API_KEY'] = "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"
documents = SimpleDirectoryReader('chatdata').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)
resp = index.query("Who are Kevin's fans?")
print(resp)