from fastapi import WebSocket, APIRouter
from app.services.iqoption_service import *
import json
import time

router = APIRouter()

start_candles_stream()


@router.websocket_route("/ws")
async def echo_socket(websocket: WebSocket):
    await websocket.accept()
    while True:
        chunk = json.dumps(get_real_time_candles())
        await websocket.send_json(chunk)
        time.sleep(1)

