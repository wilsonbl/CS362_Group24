import unittest

import main_game
from main_game import Zombie
from main_game import Plant


class Test(unittest.TestCase):
    def test_zombie_pea_hit(self):
        #Create zombies to test on
        zombie1 = Zombie(1, 1, 0)
        zombie2 = Zombie(1, 1, 1)
        zombie3 = Zombie(1, 1, -1)
        zombie4 = Zombie(1, 1, 5)
        zombie5 = Zombie(1, 1, -5)
        
        #Hit zombies with a pea
        zombie1.pea_hit()
        zombie2.pea_hit()
        zombie3.pea_hit()
        zombie4.pea_hit()
        zombie5.pea_hit()

        #Assert that health has decreased by 1
        self.assertEqual(zombie1.get_health(), 0-1)
        self.assertEqual(zombie2.get_health(), 1-1)
        self.assertEqual(zombie3.get_health(), -1-1)
        self.assertEqual(zombie4.get_health(), 5-1)
        self.assertEqual(zombie5.get_health(), -5-1)


    def test_plant_shoot(self):
        #Create group of zombies
        zombie_group = set([])
        zombie_group.add(Zombie(1, 1, 10))

        #Create test plants
        plant1 = Plant(1, 1, [1, 1], 1, 1, 10)   #Lane 1
        plant2 = Plant(1, 1, [1, 1], 1, 2, 10)   #Lane 2 (no zombie there, so no pea should be added)

        #Shoot pea from plant
        plant1.shoot(zombie_group)
        plant2.shoot(zombie_group)

        #Assert that pea has been added to pea group and is in the proper position
        self.assertEqual(len(main_game.pea_group), 1)
        self.assertEqual(main_game.pea_group.pop().get_pos(), [1 + main_game.pea_direction[0], 1 - main_game.pea_direction[1]])


if __name__ == '__main__':
    unittest.main()