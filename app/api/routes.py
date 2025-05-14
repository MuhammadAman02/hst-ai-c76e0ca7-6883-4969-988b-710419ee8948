from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chatbot_service import chatbot

router = APIRouter()

class ChatMessage(BaseModel):
    message: str

@router.get('/ping')
async def ping_pong():
    """A simple ping endpoint."""
    return {"message": "pong!"}

@router.post('/chat')
async def chat(chat_message: ChatMessage):
    """Process a chat message and return a response."""
    response = chatbot.process_message(chat_message.message)
    return {"response": response}

# Add additional API routes here using the @router decorator