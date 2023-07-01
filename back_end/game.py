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

map_size = None  # Taille de la carte
map = None  # Instance de la classe Map
player = None  # Instance de la classe Player

def initializeGame():
    """
    Initialise le jeu en créant une carte, un joueur et des événements possibles sur la carte.
    """
    global map_size, map, player  # Utilise les variables globales

    map_size = (10, 10)  # Définit la taille de la carte
    map = Map(map_size[0], map_size[1])  # Crée une instance de la classe Map avec la taille spécifiée
    player = Player("Joueur", 100, 10, 10, 10)  # Crée une instance de la classe Player avec des caractéristiques prédéfinies

    # Liste des événements possibles sur la carte
    events = [
        None,
        None,
        PotionItem(20),
        SwordItem("Épée normal", 25),
        SwordItem("Excalibur", 999),
        Enemy("Blind dragon", 200, 0),
        Enemy("Dragon", 200, 50),
        Enemy("Gobelin", 15, 5),
        Enemy("Gobelin", 15, 5)
    ]

    map.populate(events)  # Place les événements sur la carte

async def handle_move(websocket, direction):
    """
    Gère le déplacement du joueur sur la carte en fonction de la direction spécifiée.
    """
    if player is None:
        await websocket.send(json.dumps({"error": "Le jeu n'a pas été initialisé"}))
        return

    current_position = (0, 0)  # Position actuelle du joueur
    end_position = (map_size[0] - 1, map_size[1] - 1)  # Position finale de la carte

    # Mise à jour de la position en fonction de la direction spécifiée
    if direction == "up" and current_position[0] > 0:
        current_position = (current_position[0] - 1, current_position[1])
    elif direction == "down" and current_position[0] < map_size[0] - 1:
        current_position = (current_position[0] + 1, current_position[1])
    elif direction == "left" and current_position[1] > 0:
        current_position = (current_position[0], current_position[1] - 1)
    elif direction == "right" and current_position[1] < map_size[1] - 1:
        current_position = (current_position[0], current_position[1] + 1)

    event = map.grid[current_position[0]][current_position[1]]  # Événement sur la case actuelle du joueur

    if isinstance(event, AbstractItem):
        player.add_item(event)
        player.use_item(event)
        message = "Vous avez trouvé un objet : " + event.name + " et vous l'avez utilisé."
    elif isinstance(event, Enemy):
        message = "Vous avez rencontré un ennemi : " + event.name + "." + " Que voulez-vous faire ?"
    elif event is None:
        message = "Vous avez avancé sans encombre."

    # Vérifie si le joueur a atteint la position finale de la carte sans être mort
    if current_position == end_position and not player.is_dead():
        await websocket.send(json.dumps({"state": WIN, "message": "Victoire !"}))
        return

    await websocket.send(json.dumps({"player": player.__dict__, "message": message, "state": ALIVE}))

async def handle_event(websocket, action):
    """
    Gère les actions du joueur en réponse à un événement rencontré.
    """
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
    """
    Gestionnaire principal des messages reçus par le serveur WebSocket.
    """
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
