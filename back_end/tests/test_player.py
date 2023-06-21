import unittest
import sys
sys.path.append('..')

from classe.Player import Player
from classe.Enemy import Enemy
from classe.SwordItem import SwordItem
from classe.PotionItem import PotionItem

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player("John", 100, 50, 20, 30)
        self.strongEnemy = Enemy("Dragon", 9999, 10)
        self.weakEnemy = Enemy("Hyène", 30, 50)

    def test_character_initialization(self):
        self.assertEqual(self.player.name, "John")
        self.assertEqual(self.player.health, 100)
        self.assertEqual(self.player.strength, 50)
        self.assertEqual(self.player.agility, 20)
        self.assertEqual(self.player.intelligence, 30)
        self.assertEqual(self.player.items, [])

    def test_character_attack_failed(self):
        self.assertFalse(self.player.attack(self.strongEnemy))

    def test_character_attack_success(self):
        self.assertTrue(self.player.attack(self.weakEnemy))

    def test_character_defence_survived(self):
        self.assertTrue(self.player.defence(self.weakEnemy))
        # -25 hp
        self.assertEqual(self.player.health, 75)
        self.assertFalse(self.player.is_dead())

    def test_character_defence_died(self):
        self.player.health = 1
        self.assertFalse(self.player.defence(self.strongEnemy))
        self.assertTrue(self.player.is_dead())

    def test_character_escape_success(self):
        self.assertTrue(self.player.escape(self.strongEnemy))

    def test_character_escape_failed(self):
        self.assertFalse(self.player.escape(self.weakEnemy))

    def test_character_is_dead(self):
        self.assertFalse(self.player.is_dead())
        self.player.health = 0
        self.assertTrue(self.player.is_dead())
        self.player.health = -1
        self.assertTrue(self.player.is_dead())

    def test_character_add_item(self):
        swordItem = SwordItem("Excalibur", 10)
        potionItem = PotionItem(20)
        items = [swordItem, potionItem]

        self.player.add_item(swordItem)
        self.player.add_item(potionItem)

        self.assertEqual(self.player.items[0].name, items[0].name)
        self.assertEqual(self.player.items, items)

    def test_character_use_item(self):
        swordItem = SwordItem("Excalibur", 10)
        potionItem = PotionItem(20)
        beforeStrength = self.player.strength
        beforeHealth = self.player.health

        self.player.add_item(swordItem)
        self.player.add_item(swordItem)
        self.player.add_item(potionItem)

        self.player.use_item(swordItem)
        self.player.use_item(potionItem)

        self.assertEqual(self.player.strength, beforeStrength + swordItem.strength)
        self.assertEqual(self.player.health, beforeHealth + potionItem.health)

if __name__ == '__main__':
    unittest.main()
