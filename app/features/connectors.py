from fastapi import APIRouter, WebSocket

router = APIRouter(tags=['ChatRoom'])

@router.websocket('/ws')
async def websocket_endpoint(websocket : WebSocket)