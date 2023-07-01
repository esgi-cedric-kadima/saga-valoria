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

WIN = 2
ALIVE = 1
DEAD = 0

map_size = NONE
map = None
player = None

def initializeGame():
    map_size = (10, 10)
    map = Map(map_size[0], map_size[1])
    player = Player("Joueur", 100, 10, 10, 10)  # Exemple : un joueur avec 100 de santé et 10 de force, agilité et intelligence
    # Liste des événements possibles sur la carte
    events = [None, None, PotionItem(20), SwordItem("Épée normal", 25), SwordItem("Excalibur", 999), Enemy("Blind dragon", 200, 0), Enemy("Dragon", 200, 50), Enemy("Gobelin", 15, 5), Enemy("Gobelin", 15, 5)]
    map.populate(events)  # On place les événements sur la carte

async def handle_move(websocket, direction):
    if player is None:
        await websocket.send(json.dumps({"error": "Le jeu n'a pas été initialisé"}))
        return

    current_position = (0, 0)
    end_position = (map_size[0] - 1, map_size[1] - 1)

    if direction == "up" and current_position[0] > 0:
        current_position = (current_position[0] - 1, current_position[1])
    elif direction == "down" and current_position[0] < map_size[0] - 1:
        current_position = (current_position[0] + 1, current_position[1])
    elif direction == "left" and current_position[1] > 0:
        current_position = (current_position[0], current_position[1] - 1)
    elif direction == "right" and current_position[1] < map_size[1] - 1:
        current_position = (current_position[0], current_position[1] + 1)

    event = map.grid[current_position[0]][current_position[1]]

    if isinstance(event, AbstractItem):
        player.add_item(event)
        player.use_item(event)
        message = "Vous avez trouvé un objet : " + event.name + " et vous l'avez utilisé."
    elif isinstance(event, Enemy):
    elif event is None:

    if current_position == end_position and not player.is_dead():
        await websocket.send(json.dumps({"state": WIN, "message": "Victoire !"}))
        return

    await websocket.send(json.dumps(player.__dict__))

async def handle_event(websocket, action):
    if player is None:
        await websocket.send(json.dumps({"error": "Le jeu n'a pas été initialisé"}))
        return

    if action == "attack":
        if player.attack(event):
            message = "Vous avez attaqué " + event.name + " et vous l'avez tué."
        else:
            message = "Vous avez attaqué " + event.name + " mais il vous a attaqué aussi."
    elif action == "defence":
        if player.defence(event):
            message = "Vous avez défendu contre " + event.name + " et vous avez survécu."
        else:
            message = "Vous avez défendu contre " + event.name + " mais il vous a tué."
    elif action == "escape":
        if player.escape(event):
            message = "Vous avez fui " + event.name + " et vous avez survécu."
        else:
            message = "Vous avez fui " + event.name + " mais il vous a tué."

    if(player.is_dead()):
        await websocket.send(json.dumps({"state": DEAD, "message": message}))
    else:
        await websocket.send(json.dumps({"state": ALIVE, "message": message}))

async def handler(websocket):
    async for message in websocket:
        if message == "start":
            initialize_game()
            print('Game initialized')
            await websocket.send(json.dumps({"player": player.__dict__, "map": map.__dict__}))
        elif message == "move":
            data = json.loads(message)
            direction = data["direction"]
            await handle_move(websocket, direction)
         elif message == "handle_event":
            data = json.loads(message)
            action = data["action"]
            await handle_event(websocket, action)

async def main():
    async with websockets.serve(handler, "", 8001):
        print("Server started at port 8001")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())