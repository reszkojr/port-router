from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

import uvicorn

app = FastAPI()

@app.get('/')
def app():
    return "app1"

if __name__ == '__main__':
    uvicorn.run("test-api1:app", host="0.0.0.0", port=1, reload=True)