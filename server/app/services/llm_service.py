import os
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

load_dotenv()

endpoint = "https://models.github.ai/inference"
token = os.getenv("GITHUB_TOKEN")
model = "openai/gpt-5-nano"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token)
)

async def ask_llm(query: str):
    response = client.complete(
        messages=[
            SystemMessage("You are a helpful assistant. help the user for medical assistance. instructions: give short and precise answers."),
            UserMessage(query)
        ],
        model=model
    )

    return response.choices[0].message.content
