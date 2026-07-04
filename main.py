from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.features.connectors import router as ChatRoomRouter
from app.utilities.helpers import html

app = FastAPI(title="MessageX")

app.include_router(ChatRoomRouter)

@app.get('/')
async def get():
    return HTMLResponse(html)