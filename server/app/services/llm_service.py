import os
from pathlib import Path
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Load .env file from server directory
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

endpoint = "https://models.github.ai/inference"
token = os.getenv("GITHUB_TOKEN")
# Model format for GitHub AI - gpt-4o-mini works!
model = os.getenv("MODEL_NAME", "gpt-4o-mini")  # Default working model

# Initialize client lazily to avoid errors at import time
_client = None

def get_client():
    global _client
    if _client is None:
        if not token or token == "your_github_token_here":
            raise ValueError("GITHUB_TOKEN is not set. Please set it in the .env file.")
        _client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token)
        )
    return _client

async def ask_llm(query: str):
    try:
        client = get_client()
        response = client.complete(
            messages=[
                SystemMessage("You are a helpful assistant. help the user for medical assistance. instructions: give short and precise answers. only provide details regarding health and medication."),
                UserMessage(query)
            ],
            model=model
        )

        return response.choices[0].message.content
    except Exception as e:
        error_msg = str(e)
        # Provide more helpful error messages
        if "401" in error_msg or "Unauthorized" in error_msg:
            return "Error: Invalid or expired GitHub token. Please check your GITHUB_TOKEN in the .env file."
        elif "404" in error_msg or "Not Found" in error_msg or "unknown_model" in error_msg.lower():
            return f"Error: Model '{model}' not found. Try setting MODEL_NAME in .env to 'gpt-4o-mini' or another available model."
        elif "403" in error_msg or "Forbidden" in error_msg:
            return "Error: Access forbidden. Your token may not have the required permissions."
        else:
            return f"Error: {error_msg}. Please check your configuration and try again."
