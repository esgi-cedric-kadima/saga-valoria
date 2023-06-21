#!/usr/bin/env python
import asyncio
import websockets
import json
from classe.Player import Player
from classe.Map import Map

async def handler(websocket):
    player = Player("John", 100, 50, 20, 30)
    async for message in websocket:
        await websocket.send(json.dumps(player.__dict__))

async def main():
    map = Map(10, 10)
    print(map.grid)
#     map.populate(['1', '2', '3'])
    print(map.grid[(2, 2)])
    async with websockets.serve(handler, "", 8001):
        print("Server started at port 8001")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())