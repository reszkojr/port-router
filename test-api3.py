from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def api(request: Request):
    return templates.TemplateResponse("api.html", {"request": request, "api": 3})

if __name__ == '__main__':
    uvicorn.run("test-api3:app", host="0.0.0.0", port=3, reload=True)