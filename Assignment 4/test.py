import unittest

import main_game
from main_game import Zombie
from main_game import Plant


class Test(unittest.TestCase):
    def test_zombie_pea_hit(self):
        # Create zombies
        zombie1 = Zombie(1, 1, 0)
        zombie2 = Zombie(1, 1, 1)
        zombie3 = Zombie(1, 1, -1)
        zombie4 = Zombie(1, 1, 5)
        zombie5 = Zombie(1, 1, -5)
        
        # Hit zombies with peas
        zombie1.pea_hit()
        zombie2.pea_hit()
        zombie3.pea_hit()
        zombie4.pea_hit()
        zombie5.pea_hit()

        # Assert that health of each zombie has decreased by 1
        self.assertEqual(zombie1.get_health(), 0-1)
        self.assertEqual(zombie2.get_health(), 1-1)
        self.assertEqual(zombie3.get_health(), -1-1)
        self.assertEqual(zombie4.get_health(), 5-1)
        self.assertEqual(zombie5.get_health(), -5-1)


    def test_plant_shoot(self):
        # Create zombies
        zombie_group = set([])
        zombie_group.add(Zombie(1, 1, 10))
        zombie_group.add(Zombie(1, 2, 10))
        zombie_group.add(Zombie(1, 2, 10))
        zombie_group.add(Zombie(1, 4, 10))
        zombie_group.add(Zombie(1, 5, 10))
        zombie_group.add(Zombie(1, 5, 10))

        #Create plants
        plant1 = Plant(1, 1, [1, 1], 1, 1, 10)   # Lane 1 | 1 zombie, 1 plant. 1 pea should be added
        plant2 = Plant(1, 1, [1, 1], 1, 2, 10)   # Lane 2 | 2 zombies, 1 plant. 1 pea should be added
        plant3 = Plant(1, 1, [1, 1], 1, 3, 10)   # Lane 3 | 0 zombies, 1 plant. 0 peas should be added
        plant4 = Plant(1, 1, [1, 1], 1, 4, 10)   # Lane 4 | 1 zombie, 2 plants. 2 peas should be added
        plant5 = Plant(1, 1, [1, 1], 1, 4, 10)
        plant6 = Plant(1, 1, [1, 1], 1, 5, 10)   # Lane 5 | 2 zombies, 2 plants. 2 peas should be added
        plant7 = Plant(1, 1, [1, 1], 1, 5, 10)
                                                 # Grand total: 6 peas

        #Shoot peas from plants
        plant1.shoot(zombie_group)
        plant2.shoot(zombie_group)
        plant3.shoot(zombie_group)
        plant4.shoot(zombie_group)
        plant5.shoot(zombie_group)
        plant6.shoot(zombie_group)
        plant7.shoot(zombie_group)

        #Assert that correct number of peas have been added to pea group
        self.assertEqual(len(main_game.pea_group), 6)

        #Assert that each pea is in the proper position
        while len(main_game.pea_group) > 0:
            self.assertEqual(main_game.pea_group.pop().get_pos(), [1 + main_game.pea_direction[0], 1 - main_game.pea_direction[1]])
       
    def test_plant_lose_health(self):
        # Create plants
        # (sun_cost, image, pos, tower_indicator, lane, health)
        plant1 = Plant(1, 1, [1, 1], 1, 1, 10)
        plant2 = Plant(1, 1, [1, 1], 1, 1, 5)
        plant3 = Plant(1, 1, [1, 1], 1, 1, 1)
        plant4 = Plant(1, 1, [1, 1], 1, 1, -1)
        plant5 = Plant(1, 1, [1, 1], 1, 1, 10)
        
        # Create zombies
        # (pos, lane, health)
        zombie1 = Zombie(1, 1, 10)  
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
        zombie1 = Zombie([1, 1], 1, 10)
        zombie2 = Zombie([41, 1], 1, 10)
        zombie3 = Zombie([42, 1], 1, 10)
        zombie4 = Zombie([41, 1], 2, 10)
        zombie5 = Zombie([42, 1], 2, 10)
        
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
        
      def test_shovel_remove_plant(self):
        # Create Plants
        plant1 = Plant(1, 1, [1, 1], 1, 1, 10)   # Lane 1 | Position 1
        main_game.plant_group.add(plant1)
        plant2 = Plant(1, 1, [2, 2], 1, 2, 10)   # Lane 2 | Position 2
        main_game.plant_group.add(plant2)
        plant3 = Plant(1, 1, [9, 5], 1, 3, 10)   # Lane 3 | Position 3
        main_game.plant_group.add(plant3)        
        plant4 = Plant(1, 1, [50, 50], 1, 4, 10)   # Lane 4 | Position 4
        main_game.plant_group.add(plant4)        
        plant5 = Plant(1, 1, [20, 20], 1, 5, 10) # Lane 20 | Position 5
        main_game.plant_group.add(plant5)

        self.assertEqual(len(main_game.plant_group), 5)
		
		# Remove Plant 1 by position
        plant_pos = [1,1]
        if plant1.get_pos()[0] == plant_pos[0] and plant1.get_pos()[1] == plant_pos[1]:
            main_game.plant_group.remove(plant1)
        self.assertEqual(len(main_game.plant_group), 5-1)

		# Remove Plant 2 by position
        plant_pos = [2,2]
        if plant2.get_pos()[0] == plant_pos[0] and plant2.get_pos()[1] == plant_pos[1]:
            main_game.plant_group.remove(plant2)
        self.assertEqual(len(main_game.plant_group), 5-2)		

		# Remove Plant 3 by position
        plant_pos = [9,5]
        if plant3.get_pos()[0] == plant_pos[0] and plant3.get_pos()[1] == plant_pos[1]:
            main_game.plant_group.remove(plant3)
        self.assertEqual(len(main_game.plant_group), 5-3)	

		# Remove Plant 4 by position
        plant_pos = [50,50]
        if plant4.get_pos()[0] == plant_pos[0] and plant4.get_pos()[1] == plant_pos[1]:
            main_game.plant_group.remove(plant4)
        self.assertEqual(len(main_game.plant_group), 5-4)
		
		# Remove Plant 5 directly
        main_game.plant_group.remove(plant5)
        self.assertEqual(len(main_game.plant_group), 5-5)

		
     def test_place_plant(self):
		# Test costs for seeds
        main_game.sun_count = 25
        self.assertEqual(main_game.sun_count, 25)
		
		
        # Test seeds are planted in 5x9 grid
        plant1 = Plant(1, 1, [1, 1], 1, 1, 10)   # Lane 1
        main_game.plant_group.add(plant1)
        plant2 = Plant(1, 1, [2, 4], 1, 2, 10)   # Lane 2
        main_game.plant_group.add(plant2)
        plant3 = Plant(1, 1, [3, 3], 1, 3, 10)   # Lane 3
        main_game.plant_group.add(plant3)        
        plant4 = Plant(1, 1, [4, 7], 1, 4, 10)   # Lane 4
        main_game.plant_group.add(plant4)        
        plant5 = Plant(1, 1, [20, 20], 1, 5, 10) # Lane 20 | Invalid Position
        main_game.plant_group.add(plant5)
		
        self.assertEqual(len(main_game.plant_group), 5)

        plant_count = 0
        for i in range(1,5):
            for j in range(1,9):
                for plant in main_game.plant_group:
                    if plant.get_pos()[0] == i and plant.get_pos()[1] == j:
                        plant_count = plant_count + 1
        
        self.assertEqual(len(main_game.plant_group), 4)       
        
        

if __name__ == '__main__':
    unittest.main()
