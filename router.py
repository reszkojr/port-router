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

databases = [
    'Stage',
    'Helisul (pesado esse hein)',
    'Azul',
    'EPA',
]

instances = [
    None, # erp1
    None, # erp2
    None, # erp3
    None, # erp4
]

ip_hub = {}


templates = Jinja2Templates(directory="templates")

@app.get('/')
def router(request: Request):
    ip = request.client.host
    context = {
        "request": request,
        "ip": ip,
        "branches": branches,
        "dbs": databases,
        "instances": instances
        }

    return templates.TemplateResponse("router.html", context)