from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()

# Configure Jinja2 templates
templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
templates = Jinja2Templates(directory=templates_dir)

@router.get("/")
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})