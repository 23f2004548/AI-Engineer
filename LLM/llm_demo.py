import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(override=True)

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
	raise RuntimeError("Missing GOOGLE_API_KEY. Add it to .env or environment variables.")


model = ChatGoogleGenerativeAI(
	model="gemini-2.5-flash",
	
)

result = model.invoke("What is los zetas ?")
print(result.content)