from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import chat_router
import os

app = FastAPI()

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Chatbot Route
app.include_router(chat_router.router)

# Serve static files (frontend)
frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
def home():
    # Serve the chatbox HTML file
    frontend_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "frontend", "index.html")
    if os.path.exists(frontend_file):
        return FileResponse(frontend_file)
    return {"message": "LLM Chat API running! Visit /chatbox to access the chat interface."}

@app.get("/chatbox")
def chatbox():
    # Serve the chatbox HTML file
    frontend_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "frontend", "index.html")
    if os.path.exists(frontend_file):
        return FileResponse(frontend_file)
    return {"message": "Chatbox interface not found. Please create frontend/index.html"}
