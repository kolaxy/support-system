from fastapi import FastAPI, WebSocket
import asyncio


app = FastAPI()


@app.get("/")
async def get():
    return {"key": "value"}
