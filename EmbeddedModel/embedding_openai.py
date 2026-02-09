from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from torch import embedding

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embeddings-3-large", dimensions=32)
result = embedding.embed_query("What is los zetas ?")
print(result)