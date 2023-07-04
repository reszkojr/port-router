from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, Response
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

instances = {'erp1': 0, 'erp2': 0, 'erp3': 0, 'erp4': 0}


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

@app.post('/')
def redirect(instance: str = Form(...)):
    return Response(status_code=302, headers={"Location": f"/{instance}"})

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("router:app", host="0.0.0.0", port=8000, reload=True, proxy_headers=True)