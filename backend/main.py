from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

Ollama_Local_Url = "http://localhost:11434/v1/"
Ollama_Cloud_Url = "https://ollama.com/v1"

client = OpenAI(api_key=os.getenv("OLLAMA_API_KEY"), base_url=Ollama_Cloud_Url)

chat_completion = client.chat.completions.create(
    model="gpt-oss:20b-cloud",
    messages=[
        {
            "role": "user",
            "content": "This is a test message to check if the Ollama API is working correctly.",
        }
    ],
)

print(chat_completion.choices[0].message.content)
