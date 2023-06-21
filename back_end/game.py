# #!/usr/bin/env python
# import asyncio
# import websockets
# from classe.CharacterClass import Character
# from classe.MapClass import Map
# import json
#
# async def handler(websocket):
#     while True:
#         message = await websocket.recv()
#         print(message)
#
#         NewMap = Map(10, 10)
#         await websocket.send(json.dumps({'NewMap': NewMap}))
#
# async def main():
#     async with websockets.serve(handler, "", 8002):
#         await asyncio.Future()  # run forever
#
# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import json

import websockets

from back_end.classe.MapClass import Map


async def handle_client(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            print("Received from client:", message)

            # Envoyer une réponse au client
            response = "Hello from server!"
            await websocket.send(response)

            #Envoyer une map au client
            Newmap = Map(10, 10)
            await websocket.send(json.dumps(Newmap.__dict__))

    except websockets.ConnectionClosed:
        print("Client disconnected")

async def start_server():
    server = await websockets.serve(handle_client, "localhost", 8001)
    print("Server started and listening on ws://localhost:8001")

    # Garder le serveur en cours d'exécution
    await server.wait_closed()

asyncio.run(start_server())
