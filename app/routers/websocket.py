from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.iqoption_service import *
import json
import time


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)


router = APIRouter()
manager = ConnectionManager()
start_candles_stream()


@router.websocket_route("/ws")
async def get_candles(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            chunk = get_real_time_candles()
            for item in chunk:
                await websocket.send_json(item)
            time.sleep(1)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

