#!/usr/bin/env python
import asyncio
import websockets
from back_end.classe.CharacterClass import Character

if __name__ == "__main__":
    main()

async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)

async def main():
    Player = Character("Player", 100, 10, 10, 10)
    print(f"Player a {Player.health} points de vie.")
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())