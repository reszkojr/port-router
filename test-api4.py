from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

import uvicorn

app = FastAPI()

@app.get('/')
def app():
    return "app4"

if __name__ == '__main__':
    uvicorn.run("test-api4:app", host="0.0.0.0", port=4, reload=True)