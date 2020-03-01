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
       
    def test_plant_lose_health(self):
        # Create plants
        plant1 = Plant(1, 1, [1, 1], 1, 1, 10)  # (sun_cost, image, pos, tower_indicator, lane, health)
        plant2 = Plant(1, 1, [1, 1], 1, 1, 5)
        plant3 = Plant(1, 1, [1, 1], 1, 1, 1)
        plant4 = Plant(1, 1, [1, 1], 1, 1, -1)
        plant5 = Plant(1, 1, [1, 1], 1, 1, 10)
        
        # Create zombies
        zombie1 = Zombie(1, 1, 10)  # (pos, lane, health)
        zombie2 = Zombie(1, 1, 0)
        
        # Have plants get hit
        plant1.hit(zombie1)
        plant2.hit(zombie1)
        plant3.hit(zombie1)
        plant4.hit(zombie1)
        plant5.hit(zombie2)
        
        # Assert that plant health has been decremented
        self.assertEqual(plant1.get_health(), 10-1)
        self.assertEqual(plant2.get_health(), 5-1)
        self.assertEqual(plant3.get_health(), 1-1)
        self.assertEqual(plant4.get_health(), -1-1)
        self.assertEqual(plant5.get_health(), 10-1)
        
        # Assert that hit_indicator has been correctly updated
        self.assertEqual(plant1.hit_indicator, True)
        self.assertEqual(plant2.hit_indicator, True)
        self.assertEqual(plant3.hit_indicator, True)
        self.assertEqual(plant4.hit_indicator, True)
        self.assertEqual(plant5.hit_indicator, False)
        
    def test_plant_collide_with_zombie(self):
        # Create plants
        plant1 = Plant(1, 1, [1, 1], 1, 1, 10)
        
        # Create zombies
        zombie1 = Zombie(1, 1, 10)
        zombie2 = Zombie(41, 1, 10)
        zombie3 = Zombie(42, 1, 10)
        zombie4 = Zombie(41, 2, 10)
        zombie5 = Zombie(42, 2, 10)
        
        # Collide zombies and plant
        collision1 = plant1.collide(zombie1)
        collision2 = plant1.collide(zombie2)
        collision3 = plant1.collide(zombie3)
        collision4 = plant1.collide(zombie4)
        collision5 = plant1.collide(zombie5)
        
        # Assert that collisions were detected correctly
        self.assertEqual(collision1, True)
        self.assertEqual(collision2, True)
        self.assertEqual(collision3, False)
        self.assertEqual(collision4, False)
        self.assertEqual(collision5, False)

if __name__ == '__main__':
    unittest.main()
