from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..core.text import modify_text

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/", response_class=HTMLResponse)
async def submit_form(request: Request, text: str = Form(default="")):
    result_text = modify_text(text=text)
    return templates.TemplateResponse("index.html", {"request": request, "original_text": text, "result_text": result_text})
