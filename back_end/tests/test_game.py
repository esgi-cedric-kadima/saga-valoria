import unittest
import asyncio
import websockets
import json
import random

class WebSocketServerTest(unittest.TestCase):
    def setUp(self):
        self.websocket = None

    def tearDown(self):
        if self.websocket:
            asyncio.get_event_loop().run_until_complete(self.websocket.close())

    async def connect(self):
        self.websocket = await websockets.connect('ws://localhost:8001')

    async def send_message(self, message):
        await self.websocket.send(json.dumps(message))

    async def receive_message(self):
        message = await self.websocket.recv()
        return json.loads(message)

    def test_start_game(self):
        async def test():
            await self.connect()

            start_message = {"action": "start"}
            await self.send_message(start_message)
            response = await self.receive_message()

            # Vérifier la réponse du serveur
            self.assertIn("player", response["result_game_start"])
            self.assertIn("game_map", response["result_game_start"])
            self.assertIn("exit", response["result_game_start"])

        asyncio.get_event_loop().run_until_complete(test())

    def test_move_direction(self):
        async def test():
            await self.connect()

            start_message = {"action": "start"}
            await self.send_message(start_message)
            response = await self.receive_message()

            move_message = {"action": "move", "direction": "right"}
            await self.send_message(move_message)
            response = await self.receive_message()
            # Vérifier la réponse du serveur
            self.assertIn("player", response["result_move"])
            self.assertIn("message", response["result_move"])
            self.assertIn("state", response["result_move"])

        asyncio.get_event_loop().run_until_complete(test())

    def test_game_scenario(self):
        WIN = 2
        ALIVE = 1
        DEAD = 0

        async def test():
            await self.connect()

            start_message = {"action": "start"}
            await self.send_message(start_message)
            response = await self.receive_message()

            self.assertIn("player", response["result_game_start"])
            self.assertIn("game_map", response["result_game_start"])
            self.assertIn("exit", response["result_game_start"])

            player = response["result_game_start"]["player"]
            state = ALIVE
            game_map = response["result_game_start"]["game_map"]
            current_position = [0, 0]
            directions = ["up", "down", "left", "right"]
            actions = ["attack", "defence", "escape"]

            while state == ALIVE:
                # Choix aléatoire de la direction
                direction = random.choice(directions)

                move_message = {"action": "move", "direction": direction}
                await self.send_message(move_message)
                response = await self.receive_message()
                data = response
                # error return false test
                if("error" in data["result_move"]):
                    continue
                else:
                    state = response["result_move"]["state"]

                if(state == WIN):
                    break

                player = response["result_move"]["player"]

                if(direction == "up"):
                    current_position[1] = current_position[1] + 1
                elif(direction == "down"):
                    current_position[1] = current_position[1] - 1
                elif(direction == "left"):
                    current_position[0] = current_position[0] - 1
                elif(direction == "right"):
                    current_position[0] =  current_position[0] + 1

                if(game_map['grid'][current_position[0]][current_position[1]] is not None and game_map['grid'][current_position[0]][current_position[1]]['class'] == 'Enemy'):
                    action = random.choice(actions)
                    # we are strong so we attack :)
                    if(player['strength'] > 1000):
                        action = "attack"
                    action_message = {"action": "handle_event", "choice": action}
                    await self.send_message(action_message)
                    response = await self.receive_message()
                    data = response
                    player = data["result_event_action"]["player"]
                    state = data["result_event_action"]["state"]

            self.assertTrue(state in [DEAD, WIN])

        asyncio.get_event_loop().run_until_complete(test())

if __name__ == "__main__":
    unittest.main()
