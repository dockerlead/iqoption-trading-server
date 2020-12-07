from app.settings import *
import uvicorn
from fastapi import FastAPI
from app.routers import root, websocket

server = FastAPI()

server.include_router(root.router)
server.include_router(websocket.router)


if __name__ == '__main__':
    uvicorn.run("main:server", reload=True, host='0.0.0.0', port=8000, access_log=True)
