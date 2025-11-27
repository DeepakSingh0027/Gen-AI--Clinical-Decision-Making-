from fastapi import APIRouter, HTTPException
from app.schemas.chat_schema import ChatRequest
from app.services.llm_service import ask_llm

router = APIRouter(prefix="/chat", tags=["Chatbot"])

@router.post("/")
async def chat_endpoint(payload: ChatRequest):
    try:
        message = payload.message
        llm_reply = await ask_llm(message)
        return {"response": llm_reply}
    except Exception as e:
        error_msg = str(e)
        # Return a user-friendly error message
        return {
            "response": f"Error: {error_msg}. Please check your GITHUB_TOKEN and API configuration."
        }
