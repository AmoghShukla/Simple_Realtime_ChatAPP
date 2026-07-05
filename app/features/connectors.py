from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from app.utilities.websockets import manager
import random
from app.utilities.helpers import html

router = APIRouter(tags=["ChatRoom"])

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    client_id = random.randint(111111111, 999999999)

    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            
            await manager.broadcast(
                f"Client #{client_id}: {data}"
            )

    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        await manager.broadcast(
            f"Client #{client_id} has left the chat."
        )