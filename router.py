from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

branches = [
    'ERP1',
    'ERP2',
    'ERP3',
]

ip_hub = {}

templates = Jinja2Templates(directory="templates")

@app.get('/')
def router(request: Request):
    ip = request.client.host

    return templates.TemplateResponse("router.html", {"request": request, "ip": ip})