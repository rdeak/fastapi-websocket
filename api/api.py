from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict
from .acknowledge_job import acknowledge_job

app = FastAPI()

active_connections: Dict[str, WebSocket] = {}


@app.websocket("/ws/{token}")
async def incoming_message(websocket: WebSocket, token: str):
    await websocket.accept()

    # validate token
    if token == "1":
        await websocket.close(code=4001, reason="Unauthenticated access")
        return

    active_connections[token] = websocket

    try:
        while True:
            data = await websocket.receive_text()

            response = await acknowledge_job(
                data
            )

            await send_response(token, response)
    except WebSocketDisconnect:
        del active_connections[token]


async def send_response(token: str, message: str):
    if token in active_connections:
        await active_connections[token].send_text(message)
