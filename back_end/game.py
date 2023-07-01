#!/usr/bin/env python
import asyncio
import websockets
import json

# classes
from classe.Character import Character
from classe.Enemy import Enemy
from classe.Map import Map
from classe.Player import Player
from classe.PotionItem import PotionItem
from classe.SwordItem import SwordItem

map = None
player = None

def initializeGame():
    map = Map(10, 10)
    player = Player("Joueur", 100, 10, 10, 10)  # Exemple : un joueur avec 100 de santé et 10 de force, agilité et intelligence
    # Liste des événements possibles sur la carte
    events = [None, None, PotionItem(20), SwordItem("Épée puissante", 25), Enemy("Dragon", 20, 15)]
    map.populate(events)  # On place les événements sur la carte

async def handler(websocket):
    async for message in websocket:
        await websocket.send(json.dumps(player.__dict__))

async def main():
    initializeGame()
    print('Game initialized')
    async with websockets.serve(handler, "", 8001):
        print("Server started at port 8001")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())