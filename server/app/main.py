from fastapi import FastAPI
from app.routes import chat_router

app = FastAPI()

# Register Chatbot Route
app.include_router(chat_router.router)

@app.get("/")
def home():
    return {"message": "LLM Chat API running!"}
