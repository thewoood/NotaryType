import uvicorn
from backend.routes.text import router
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.include_router(router=router)


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "original_text": "", "result_text": ""})


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
