import os 
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
if not api_key:
	raise RuntimeError("Missing HUGGINGFACEHUB_ACCESS_TOKEN in .env or environment variables.")
if api_key.startswith("hf_") is False:
	raise RuntimeError("HUGGINGFACEHUB_ACCESS_TOKEN looks invalid. Replace it with a real token.")

llm = HuggingFaceEndpoint(
	repo_id="inference-net/Schematron-3B",
	task="text2text-generation",
	provider="hf-inference",
	huggingfacehub_api_token=api_key,
)
result = llm.invoke("Who are Los Zetas and where did they expand their network?")
print(result)