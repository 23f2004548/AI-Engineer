from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
model =ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature = 0, max_completion_tokens = 20 )
result = model.invoke("write a 5 line poem on cricket")
print(result.content)