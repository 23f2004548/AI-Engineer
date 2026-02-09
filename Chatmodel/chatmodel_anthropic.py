from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

model = ChatAnthropic(model="claude-2", temperature=0.5, max_tokens=100)
result = model.invoke("What is los zetas ?")    
print(result.content)