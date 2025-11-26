from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.services.llm_service import ask_llm

router = APIRouter(prefix="/chat", tags=["Chatbot"])

@router.post("/")
async def chat_endpoint(payload: ChatRequest):
    message = payload.message
    llm_reply = await ask_llm(message)
    return {"response": llm_reply}
