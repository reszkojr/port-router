from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

import uvicorn

app = FastAPI()

@app.get('/')
def app():
    return "app3"

if __name__ == '__main__':
    uvicorn.run("test-apis:app", host="0.0.0.0", port=3, reload=True)