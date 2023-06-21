#!/usr/bin/env python
import asyncio
import websockets
import json
from classe.Player import Player

async def handler(websocket):
    player = Player("John", 100, 50, 20, 30)
    async for message in websocket:
        await websocket.send(json.dumps(player.__dict__))

async def main():
    async with websockets.serve(handler, "", 8001):
        print("Server started at port 8001")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())