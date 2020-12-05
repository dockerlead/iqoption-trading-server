from fastapi import WebSocket

async def websocket_controller(websocket: WebSocket)
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
