from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict
from .acknowledge_job import acknowledge_job

app = FastAPI()

active_connections: Dict[str, WebSocket] = {}


@app.websocket("/ws/{user_id}")
async def incoming_message(websocket: WebSocket, user_id: str):
    await websocket.accept()
    active_connections[user_id] = websocket

    try:
        while True:
            data = await websocket.receive_text()

            await acknowledge_job(
                data,
                lambda message: send_response(user_id, message)
            )
    except WebSocketDisconnect:
        del active_connections[user_id]


async def send_response(user_id: str, message: str):
    if user_id in active_connections:
        await active_connections[user_id].send_text(message)
