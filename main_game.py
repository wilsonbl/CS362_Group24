# Plants vs. Zombies Clone
# Created by Austin Moninger in COMP 160 (Fall 2017)


#################################################################################################################
# SUBMISSION 11/18/2017)
#
# LINK TO PITCH SHEET:
# • https://www.dropbox.com/s/0fkqnbtrxi3vxky/pitchsheet.png?dl=0
#
# CONTROLS
# • collect sun by clicking
# • plant seeds by clicking once on the seed packet and then once more
#	on the playing grid (plants in the nearest location to the click)
# • sunflowers will give you more sun
# • peashooters will take down incoming zombies
# • walnuts will provide a sturdy barrier

# • second wave at score 35 and third wave at score 80
#
#################################################################################################################
# TODO
# • game balance
#################################################################################################################



# Import statements
import simplegui
import random
import math


# Size constants of images
FRAME_DIM = (1024, 626)
SEED_DIM = (288, 180)
SUN_DIM = (177, 177)
PEASHOOTER_DIM = (166, 169)
SUNFLOWER_DIM = (235, 270)
PEA_DIM = (28, 28)
ZOMBIE_DIM = (1454, 2329)
SPLASH_DIM = (509, 310)
BUTTON_DIM = (158, 154)
INSTRUCTIONS_DIM = (1358, 1000)
CONEHEAD_DIM = (139, 270)
BUCKET_DIM = (446, 774)
WALNUT_DIM = (140, 163)
WAVE_DIM = (350, 150)
SUNSCORE_DIM = (956, 160)


# Desired image sizes
desired_sun_dim = (75, 75)
desired_seed_dim = (140, 100)
desired_selectedseed_dim = (100, 70)
desired_peashooter_dim = (75, 78)
desired_sunflower_dim = (85, 90)
desired_pea_dim = (20, 20)
desired_zombie_dim = (80, 100)
desired_splash_dim = (500, 300)
desired_button_dim = (80, 80)
desired_instr_dim = (900, 550)
desired_walnut_dim = (75, 100)
desired_wave_dim = (160, 60)
desired_sunscore_dim = (360, 60)


# Constants of grid
LEFT_EDGE_GRID = 250
RIGHT_EDGE_GRID = 1000
TOP_EDGE_GRID = 50
BOTTOM_EDGE_GRID = 560
first_square = (296, 125)
dist_squares = (80, 92)


# Constants that don't change
first_seed_pos = (110, 130)
pea_vel = 5
sun_value = 25
collision_detection = 40
plant_health = 300
wave1_cap = 35
wave2_cap = 80
game_over_line = 255
sun_spawn_freq = 12000 # TODODOODOODVA
pea_shoot_freq = 1800
sunflower_spawn_freq = 15000
zombie_spawn_freq = 20000
conehead_spawn_freq = 80000
bucket_spawn_freq = 130000
zombie_groan_freq = 10000


# Constants that will change
zombie_vel = 0.18
sun_count = 100 #TODODOODOODVA
tower_indicator = 0
score = 0 #TODODOODOODVA
highscore = 0
seed_selected = False
shovel_selected = False
game_started = False
show_instr = False
show_score = False
new_wave_flash = False
new_wave_height = 0
plant_image = None
sun_cost = 0
time = 0
time2 = 0
time3 = 0
wave = 1
not_run_wave2_yet = True
not_run_wave3_yet = True
not_run_150_yet = True


#################################################################################################################



# Images
day_background_image = 		simplegui.load_image("https://www.dropbox.com/s/62atmr4nbx2ojjj/day_background.png?dl=1")
sun_image = 				simplegui.load_image("https://www.dropbox.com/s/2gjjer5e9eajedc/Sun_PvZ2.png?dl=1")
shovel_image = 				simplegui.load_image("https://www.dropbox.com/s/vc6of6ec5hu09s9/Shovel.jpg?dl=1")

sunflower_seed_image = 		simplegui.load_image("https://www.dropbox.com/s/89y58jbktvafuly/sunflowerseed.png?dl=1")
peashooter_seed_image = 	simplegui.load_image("https://www.dropbox.com/s/6ugi6meynohl47j/peashooterseed.png?dl=1")
snowpea_seed_image = 		simplegui.load_image("https://www.dropbox.com/s/bv8gap0tqkn93eh/snowpea.png?dl=1")
walnut_seed_image = 		simplegui.load_image("https://www.dropbox.com/s/enlf1u3yejgndt3/Screen%20Shot%202017-11-18%20at%203.38.10%20PM.png?dl=1")

sunflower_tower_image = 	simplegui.load_image("https://www.dropbox.com/s/fuj6bcrimir1mx0/HD_Sunflower.png?dl=1")
sunflowerhit_tower_image = 	simplegui.load_image("https://www.dropbox.com/s/o3jjmxae2me738m/litsunflower.png?dl=1")
peashooter_tower_image = 	simplegui.load_image("https://www.dropbox.com/s/0sqvo61m5tx68wh/Pea_Shooter.png?dl=1")
peashooterhit_tower_image = simplegui.load_image("https://www.dropbox.com/s/iy0ujwqgxjscg9q/hitpeashooter.png?dl=1")
snowpea_tower_image =       simplegui.load_image("https://www.dropbox.com/s/3d65rgip2ov8ukc/Snow_Pea.png?dl=1")
walnut_tower_image = 		simplegui.load_image("https://www.dropbox.com/s/bbvzhu8t2q62zio/Wall-nut-hd.png?dl=1")
walnuthit_tower_image = 	simplegui.load_image("https://www.dropbox.com/s/4b32j5zkouxgzpc/hitwalnut.png?dl=1")
oldwalnut_image = 			simplegui.load_image("https://www.dropbox.com/s/zzbyufe0inz8pnm/Wallnut_cracked1.png?dl=1")
oldwalnuthit_image = 		simplegui.load_image("https://www.dropbox.com/s/7zi86qgopqu1yrp/hitcrackedwalnut.png?dl=1")

peashadow_image = 			simplegui.load_image("https://www.dropbox.com/s/thrp9ltsn3rxty5/shadow.png?dl=1")
pea_image = 				simplegui.load_image("https://www.dropbox.com/s/56b2cfvee1z3olg/Pea.png?dl=1")
hitzombie_image = 			simplegui.load_image("https://www.dropbox.com/s/rq2kabis5plevri/hitzombie.png?dl=1")
zombie_image = 				simplegui.load_image("https://www.dropbox.com/s/lieab5uaomszh09/zombie.png?dl=1")
conehead_image =            simplegui.load_image("https://www.dropbox.com/s/a19sissrln1mmy5/conehead.png?dl=1")
coneheadhit_image = 		simplegui.load_image("https://www.dropbox.com/s/b7zh8bcyf0jps5x/coneheadhit.png?dl=1")
bucket_image = 				simplegui.load_image("https://www.dropbox.com/s/nbg9bgcvwri6mv0/zombie_buckethead.png?dl=1")
buckethit_image = 		    simplegui.load_image("https://www.dropbox.com/s/fr5ccnunhrcbsjt/bucketheadhit.png?dl=1")

splash_image =              simplegui.load_image("https://www.dropbox.com/s/fevto0xhcg5t688/plants-vs-zombies-logo.png?dl=1")
play_image = 				simplegui.load_image("https://www.dropbox.com/s/4ww4nv78r76zl0y/play.png?dl=1")
howtoplay_image = 			simplegui.load_image("https://www.dropbox.com/s/y1n0nmkm7u986qp/howtoplay.png?dl=1")
instructions_image =		simplegui.load_image("https://www.dropbox.com/s/i40ic5v4emygry3/Screen%20Shot%202017-11-18%20at%207.27.44%20PM.png?dl=1")
highscore_image =  			simplegui.load_image("https://www.dropbox.com/s/zrm1a29604m8ncd/highscore.png?dl=1")
highscore_back_image =      simplegui.load_image("https://www.dropbox.com/s/0tiz23o4atab3ci/Screen%20Shot%202017-11-18%20at%202.25.53%20PM.png?dl=1")
newgame_image = 			simplegui.load_image("https://www.dropbox.com/s/kci1dlr4mt873aj/newgame.png?dl=1")
wave_image = 				simplegui.load_image("https://www.dropbox.com/s/eoupzjx28pc0d2r/Screen%20Shot%202017-11-18%20at%208.24.26%20PM.png?dl=1")
sunscore_image = 			simplegui.load_image("https://www.dropbox.com/s/h2embumab678cjn/Screen%20Shot%202017-11-18%20at%208.24.04%20PM.png?dl=1")
cooldown_image = 			simplegui.load_image("https://www.dropbox.com/s/069bxjiifzb38s6/dark.png?dl=1")

# Music and sounds
day_soundtrack = 			simplegui.load_sound("https://www.dropbox.com/s/qzz4jvyrzuzbl5h/maintheme.mp3?dl=1")
second_soundtrack =         simplegui.load_sound("https://www.dropbox.com/s/nryvrqy0nwnr9bp/09-watery-graves-fast-.mp3?dl=1")
third_soundtrack = 			simplegui.load_sound("https://www.dropbox.com/s/d66ahu3i1dl60yr/15%20Zombies%20on%20Your%20Lawn.mp3?dl=1")

water_sound = 				simplegui.load_sound("https://www.dropbox.com/s/d4c0elop8wov3yy/waterdrop.mp3?dl=1")
eating_sound = 				simplegui.load_sound("https://www.dropbox.com/s/9mi4fisf7z2fny5/ZombieBite.ogx?dl=1")
gameover_sound = 			simplegui.load_sound("https://www.dropbox.com/s/8l8l5irddsdz5e5/Game%20Over%20-%20Plants%20vs.%20Zombies.mp3?dl=1")

groan_sound1 = 				simplegui.load_sound("https://www.dropbox.com/s/0f260vzwykdrqqj/Groan.ogx?dl=1")
groan_sound2 = 				simplegui.load_sound("https://www.dropbox.com/s/p38y0osiqqgidz0/Groan4.ogx?dl=1")
groan_sound3 = 				simplegui.load_sound("https://www.dropbox.com/s/6guppg6h8lsnqns/DinoGroan4.ogx?dl=1")
groan_sound4 = 				simplegui.load_sound("https://www.dropbox.com/s/mm5ab0vg2lpb9og/DinoGroan5.ogx?dl=1")

splat_sound1 = 				simplegui.load_sound("https://www.dropbox.com/s/1q767wojrd8gzvd/Splat.ogx?dl=1")
splat_sound2 = 				simplegui.load_sound("https://www.dropbox.com/s/1q767wojrd8gzvd/Splat.ogx?dl=1")
splat_sound3 = 				simplegui.load_sound("https://www.dropbox.com/s/1q767wojrd8gzvd/Splat.ogx?dl=1")
splat_sound4 = 				simplegui.load_sound("https://www.dropbox.com/s/1q767wojrd8gzvd/Splat.ogx?dl=1")
splat_sound5 = 				simplegui.load_sound("https://www.dropbox.com/s/1q767wojrd8gzvd/Splat.ogx?dl=1")
splat_sound6 = 				simplegui.load_sound("https://www.dropbox.com/s/1q767wojrd8gzvd/Splat.ogx?dl=1")
splat_sound7 = 				simplegui.load_sound("https://www.dropbox.com/s/1q767wojrd8gzvd/Splat.ogx?dl=1")
splat_sound8 = 				simplegui.load_sound("https://www.dropbox.com/s/1q767wojrd8gzvd/Splat.ogx?dl=1")

shoot_sound1 = 				simplegui.load_sound("https://www.dropbox.com/s/adwe6iyznkr82rd/Throw.ogx?dl=1")
shoot_sound2 = 				simplegui.load_sound("https://www.dropbox.com/s/adwe6iyznkr82rd/Throw.ogx?dl=1")
shoot_sound3 = 				simplegui.load_sound("https://www.dropbox.com/s/adwe6iyznkr82rd/Throw.ogx?dl=1")
shoot_sound4 = 				simplegui.load_sound("https://www.dropbox.com/s/adwe6iyznkr82rd/Throw.ogx?dl=1")
shoot_sound5 = 				simplegui.load_sound("https://www.dropbox.com/s/adwe6iyznkr82rd/Throw.ogx?dl=1")
shoot_sound6 = 				simplegui.load_sound("https://www.dropbox.com/s/adwe6iyznkr82rd/Throw.ogx?dl=1")
shoot_sound7 = 				simplegui.load_sound("https://www.dropbox.com/s/adwe6iyznkr82rd/Throw.ogx?dl=1")
shoot_sound8 = 				simplegui.load_sound("https://www.dropbox.com/s/adwe6iyznkr82rd/Throw.ogx?dl=1")

drop_sound1 = 				simplegui.load_sound("https://www.dropbox.com/s/d4c0elop8wov3yy/Water%20Drop-SoundBible.com-2039669379.mp3?dl=1")
drop_sound2 = 				simplegui.load_sound("https://www.dropbox.com/s/d4c0elop8wov3yy/Water%20Drop-SoundBible.com-2039669379.mp3?dl=1")
drop_sound3 = 				simplegui.load_sound("https://www.dropbox.com/s/d4c0elop8wov3yy/Water%20Drop-SoundBible.com-2039669379.mp3?dl=1")
drop_sound4 = 				simplegui.load_sound("https://www.dropbox.com/s/d4c0elop8wov3yy/Water%20Drop-SoundBible.com-2039669379.mp3?dl=1")
drop_sound5 = 				simplegui.load_sound("https://www.dropbox.com/s/d4c0elop8wov3yy/Water%20Drop-SoundBible.com-2039669379.mp3?dl=1")

digging_sound1 = 			simplegui.load_sound("http://www.freesfx.co.uk/rx2/mp3s/6/17997_1464269733.mp3?dl=1")
digging_sound2 = 			simplegui.load_sound("http://www.freesfx.co.uk/rx2/mp3s/6/17997_1464269733.mp3?dl=1")
digging_sound3 = 			simplegui.load_sound("http://www.freesfx.co.uk/rx2/mp3s/6/17997_1464269733.mp3?dl=1")
digging_sound4 = 			simplegui.load_sound("http://www.freesfx.co.uk/rx2/mp3s/6/17997_1464269733.mp3?dl=1")
digging_sound5 = 			simplegui.load_sound("http://www.freesfx.co.uk/rx2/mp3s/6/17997_1464269733.mp3?dl=1")
digging_sound6 = 			simplegui.load_sound("http://www.freesfx.co.uk/rx2/mp3s/6/17997_1464269733.mp3?dl=1")
digging_sound7 = 			simplegui.load_sound("http://www.freesfx.co.uk/rx2/mp3s/6/17997_1464269733.mp3?dl=1")
digging_sound8 = 			simplegui.load_sound("http://www.freesfx.co.uk/rx2/mp3s/6/17997_1464269733.mp3?dl=1")

sun_sound1 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")
sun_sound2 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")
sun_sound3 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")
sun_sound4 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")
sun_sound5 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")
sun_sound6 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")
sun_sound7 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")
sun_sound8 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")
sun_sound9 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")
sun_sound10 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")
sun_sound11 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")
sun_sound12 = 				simplegui.load_sound("https://www.dropbox.com/s/929r0ob0ud3xcgu/Points.oga?dl=1")

beep_sound1 = 				simplegui.load_sound("https://www.dropbox.com/s/99pncxszpzu9bfj/beep4.mp3?dl=1")
beep_sound2 = 				simplegui.load_sound("https://www.dropbox.com/s/99pncxszpzu9bfj/beep4.mp3?dl=1")
beep_sound3 = 				simplegui.load_sound("https://www.dropbox.com/s/99pncxszpzu9bfj/beep4.mp3?dl=1")
beep_sound4 = 				simplegui.load_sound("https://www.dropbox.com/s/99pncxszpzu9bfj/beep4.mp3?dl=1")
beep_sound5 = 				simplegui.load_sound("https://www.dropbox.com/s/99pncxszpzu9bfj/beep4.mp3?dl=1")



#################################################################################################################



# Image class storing center and size of the image
class ImageInfo:
    def __init__(self, center, size):
        self.center = center
        self.size = size

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size


# Class storing properties of a plant tower
class Plant:
    def __init__(self, sun_cost, image, pos, tower_indicator, lane, health):
        self.sun_cost = sun_cost
        self.image = image
        self.pos = pos
        self.bob_pos = list(pos)
        self.tower_indicator = tower_indicator
        self.lane = lane
        self.health = health
        self.timer_sun = 0
        self.angle = 0
        self.rotate_right = False
        self.timer_pea = 0
        self.bob_up = False
        self.hit_indicator = False
        self.hit_counter = 0
        self.last_hit = 0

    def get_health(self):
        return self.health

    def get_pos(self):
        return self.pos

    def get_sun_cost(self):
        return self.sun_cost

    def get_tower_indicator(self):
        return self.tower_indicator

    def sunflower_sun_spawner(self):
        sun_group.add(Sun([self.get_pos()[0], self.get_pos()[1] + 30], True))

    def not_being_hit(self):
        self.hit_indicator = False

    # Knock health when being eaten
    def hit(self, zombie):
        self.health -= 1
        self.hit_indicator = True
        self.last_hit = 0
        if zombie.get_health() <= 1:
            self.hit_indicator = False
        #self.hit_counter = 0

    # Detect collisions with zombies
    def collide(self, zombie):
        return (self.lane == zombie.get_lane() and
               math.fabs(zombie.get_pos()[0] - self.pos[0]) <= collision_detection)

    # Shoot peas
    def shoot(self, zombie_group):
        for zombie in zombie_group:
            if zombie.get_lane() == self.lane:
                pos = list(self.pos)
                pos[0] += 40
                pos[1] -= 20
                pea_group.add(Pea(pos, self.lane))
                pea_shoot()

    def draw(self, canvas):

        if self.tower_indicator == 1 or self.tower_indicator == 2:
            if self.bob_up:
                self.bob_pos[1] += 0.07
                if self.bob_pos[1] > self.pos[1] + 2:
                    self.bob_up = False
            else:
                self.bob_pos[1] -= 0.07
                if self.bob_pos[1] < self.pos[1] - 2:
                    self.bob_up = True

            if self.tower_indicator == 1:

                if self.hit_indicator:
                    self.hit_counter += 1


                if self.hit_counter % 60 < 30 and self.hit_indicator:
                    canvas.draw_image(sunflowerhit_tower_image, sunflower_info.get_center(),
                                        sunflower_info.get_size(), self.bob_pos, desired_sunflower_dim)
                else:
                    canvas.draw_image(sunflower_tower_image, sunflower_info.get_center(),
                                        sunflower_info.get_size(), self.bob_pos, desired_sunflower_dim)
                self.timer_sun += 1

                if self.timer_sun == 420 or self.timer_sun % 1320 == 0:
                    self.sunflower_sun_spawner()

            elif self.tower_indicator == 2:
                self.timer_pea += 1
                if self.timer_pea % 108 == 0:
                    self.shoot(zombie_group)
                if self.hit_indicator:
                    self.hit_counter += 1

                if self.hit_counter % 60 < 30 and self.hit_indicator:
                    canvas.draw_image(peashooterhit_tower_image, peashooter_info.get_center(),
                                    peashooter_info.get_size(), self.bob_pos, desired_peashooter_dim)
                else:
                    canvas.draw_image(peashooter_tower_image, peashooter_info.get_center(),
                                    peashooter_info.get_size(), self.bob_pos, desired_peashooter_dim)

        elif self.tower_indicator == 3:
            if self.rotate_right:
                self.angle += 0.005
                if self.angle >= 0.15:
                    self.rotate_right = False
            else:
                self.angle -= 0.005
                if self.angle <= -0.15:
                    self.rotate_right = True

            if self.hit_indicator:
                self.hit_counter += 1
            if self.health >= 600:

                if self.hit_counter % 60 < 30 and self.hit_indicator:
                    canvas.draw_image(walnuthit_tower_image, walnut_info.get_center(),
                                  walnut_info.get_size(), self.pos, desired_walnut_dim, self.angle)
                else:
                    canvas.draw_image(walnut_tower_image, walnut_info.get_center(),
                                  walnut_info.get_size(), self.pos, desired_walnut_dim, self.angle)
            else:
                if self.hit_counter % 60 < 30 and self.hit_indicator:
                    canvas.draw_image(oldwalnuthit_image, [50, 50], [100, 100], self.pos, desired_walnut_dim, self.angle)
                else:
                    canvas.draw_image(oldwalnut_image, [50, 50], [100, 100], self.pos, desired_walnut_dim, self.angle)


# Class storing properties of a zombie
class Zombie:
    def __init__(self, pos, lane, health):
        self.health = health
        self.pos = pos
        self.lane = lane
        self.hit = False
        self.hit_counter = 0

        self.rotate_right = True
        self.angle = 0.05

    def get_pos(self):
        return self.pos

    def get_health(self):
        return self.health

    def get_lane(self):
        return self.lane

    # Knock health when hit by peas
    def pea_hit(self):
        self.health -= 1
        self.hit = True
        self.hit_counter = 0

    # Move the zombie to the left
    def update(self):
        self.pos[0] -= zombie_vel

    def draw(self, canvas):
        if self.rotate_right:
            self.angle += 0.005
            if self.angle >= 0.4:
                self.rotate_right = False
        else:
            self.angle -= 0.005
            if self.angle <= -0.2:
                self.rotate_right = True

        self.hit_counter += 1

        if self.health >= 30:
            if self.hit and self.hit_counter <= 5:
                canvas.draw_image(buckethit_image, bucket_info.get_center(), bucket_info.get_size(),
                              self.pos, desired_zombie_dim, self.angle)
            else:
                canvas.draw_image(bucket_image, bucket_info.get_center(), bucket_info.get_size(),
                              self.pos, desired_zombie_dim, self.angle)
        elif self.health >= 20:
            if self.hit and self.hit_counter <= 5:
                canvas.draw_image(coneheadhit_image, conehead_info.get_center(), conehead_info.get_size(),
                              self.pos, desired_zombie_dim, self.angle)
            else:
                canvas.draw_image(conehead_image, conehead_info.get_center(), conehead_info.get_size(),
                              self.pos, desired_zombie_dim, self.angle)
        else:
            if self.hit and self.hit_counter <= 5:
                canvas.draw_image(hitzombie_image, zombie_info.get_center(), zombie_info.get_size(),
                              self.pos, desired_zombie_dim, self.angle)
            else:
                canvas.draw_image(zombie_image, zombie_info.get_center(), zombie_info.get_size(),
                            self.pos, desired_zombie_dim, self.angle)


# Class storing properties of a sun
class Sun:
    def __init__(self, pos, from_flower):
        self.pos = pos
        self.shrinking = False
        self.new_dim = list(desired_sun_dim)
        self.from_flower = from_flower
        self.angle = 0
        self.spin_left = random.choice([True, False])

    def get_pos(self):
        return self.pos

    def get_new_dim(self):
        return self.new_dim

    def is_shrinking(self):
        return self.shrinking

    def make_shrink(self):
        self.shrinking = True

    def draw(self, canvas):
        if self.spin_left:
            self.angle -= 0.01
        else:
            self.angle += 0.01

        if not self.from_flower:
            self.pos[1] += 0.5

        if self.shrinking:
            self.new_dim[0] = self.new_dim[0] * 0.9
            self.new_dim[1] = self.new_dim[1] * 0.9
            canvas.draw_image(sun_image, sun_info.get_center(), sun_info.get_size(),
                          self.pos, self.new_dim, self.angle)
        else:
            canvas.draw_image(sun_image, sun_info.get_center(), sun_info.get_size(),
                          self.pos, desired_sun_dim, self.angle)


# Class storing properties of a pea
class Pea:
    def __init__(self, pos, lane):
        self.pos = pos
        self.lane = lane

    def get_pos(self):
        return self.pos

    # Move the pea to the right
    def update(self):
        self.pos[0] += pea_vel

    # Detect collisions with zombies
    def collide(self, zombie):
        return (self.lane == zombie.get_lane() and
               math.fabs(zombie.get_pos()[0] - self.pos[0]) <= 10)

    def draw(self, canvas):
        canvas.draw_image(pea_image, pea_info.get_center(), pea_info.get_size(),
                          self.pos, desired_pea_dim)


# Class storing properties of a seed packet
class Seed:
    def __init__(self, image, selected):
        self.image = image
        self.selected = selected

    def change_selection(self):
        self.selected = not self.selected

    def draw(self, canvas, pos):
        if self.selected:
            canvas.draw_image(self.image, seed_info.get_center(), seed_info.get_size(),
                          pos, desired_selectedseed_dim)
        else:
            canvas.draw_image(self.image, seed_info.get_center(), seed_info.get_size(),
                          pos, desired_seed_dim)



#################################################################################################################



# ImageInfo of important images
day_background_info = ImageInfo([FRAME_DIM[0] / 2, FRAME_DIM[1] / 2], FRAME_DIM)
splash_info = ImageInfo([SPLASH_DIM[0] / 2, SPLASH_DIM[1] / 2], SPLASH_DIM)
seed_info = ImageInfo([SEED_DIM[0] / 2, SEED_DIM[1] / 2], SEED_DIM)
sun_info = ImageInfo([SUN_DIM[0] / 2, SUN_DIM[1] / 2], SUN_DIM)
sunflower_info = ImageInfo([SUNFLOWER_DIM[0] / 2, SUNFLOWER_DIM[1] / 2], SUNFLOWER_DIM)
peashooter_info = ImageInfo([PEASHOOTER_DIM[0] / 2, PEASHOOTER_DIM[1] / 2], PEASHOOTER_DIM)
pea_info = ImageInfo([PEA_DIM[0] / 2, PEA_DIM[1] / 2], PEA_DIM)
zombie_info = ImageInfo([ZOMBIE_DIM[0] / 2, ZOMBIE_DIM[1] / 2], ZOMBIE_DIM)
conehead_info = ImageInfo([CONEHEAD_DIM[0] / 2, CONEHEAD_DIM[1] / 2], CONEHEAD_DIM)
bucket_info = ImageInfo([BUCKET_DIM[0] / 2, BUCKET_DIM[1] / 2], BUCKET_DIM)
button_info = ImageInfo([BUTTON_DIM[0] / 2, BUTTON_DIM[1] / 2], BUTTON_DIM)
instructions_info = ImageInfo([INSTRUCTIONS_DIM[0] / 2, INSTRUCTIONS_DIM[1] / 2], INSTRUCTIONS_DIM)
walnut_info = ImageInfo([WALNUT_DIM[0] / 2, WALNUT_DIM[1] / 2], WALNUT_DIM)
wave_info = ImageInfo([WAVE_DIM[0] / 2, WAVE_DIM[1] / 2], WAVE_DIM)
sunscore_info = ImageInfo([SUNSCORE_DIM[0] / 2, SUNSCORE_DIM[1] / 2], SUNSCORE_DIM)



#################################################################################################################
# HELPER FUNCTIONS #



# Finds the distance between two points
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Create grid to place plants onto
def create_grid():
    grid_pos_group = []
    for y in range(5):
        for x in range(9):
            grid_pos_group.append([first_square[0] + dist_squares[0] * x,
                                   first_square[1] + dist_squares[1] * y])
    return grid_pos_group


# Add seed packets to the seed group
def add_seeds():
    seed_group.append(Seed(sunflower_seed_image, False))
    seed_group.append(Seed(peashooter_seed_image, False))
    seed_group.append(Seed(walnut_seed_image, False))


# new game or new wave
def reset():
    global game_started, highscore, score, zombie_vel, time, time2, time3
    global seed_selected, shovel_selected, new_wave_flash

    highscore = score
    zombie_vel = 0.18
    time = 0
    time2 = 0
    time3 = 0
    seed_selected = False
    shovel_selected = False

    sun_timer.stop()
    zombie_timer.stop()
    conehead_timer.stop()
    bucket_timer.stop()
    zombie_groan_timer.stop()


    zombie_timer2.stop()
    zombie_timer3.stop()

    wave2_zombie_timer.stop()
    wave2_conehead_timer.stop()
    wave2_bucket_timer.stop()

    wave3_zombie_timer.stop()
    wave3_conehead_timer.stop()
    wave3_bucket_timer.stop()

    score_zombie_timer.stop()
    score_conehead_timer.stop()
    score_bucket_timer.stop()

    conehead_timer.stop()
    conehead_timer2.stop()
    conehead_timer3.stop()

    bucket_timer.stop()
    bucket_timer2.stop()
    bucket_timer3.stop()

    for sun in set(sun_group):
        sun_group.remove(sun)
    for zombie in set(zombie_group):
        zombie_group.remove(zombie)
    for pea in set(pea_group):
        pea_group.remove(pea)
    for plant in set(plant_group):
        plant_group.remove(plant)

    new_wave_flash = False


#################################################################################################################
# HANDLERS #



# Mouse click handler
def mouseclick_handler(pos):
    global seed_selected, sun_count, plant_type, sun_cost, plant_image, zombie_vel, score, wave
    global tower_indicator, seed_group, game_started, show_instr, show_score, highscore, shovel_selected

    # menu buttons
    if show_instr:
        show_instr = False
        return
    elif show_score:
        show_score = False
        return
    elif (not game_started) and 370 <= pos[1] <= 450:
        if 360 <= pos[0] <= 440:
            game_started = True
            return
        elif 462 <= pos[0] <= 540:
            show_instr = True
            return
        elif 562 <= pos[0] <= 640:
            show_score = True
            return

    # Check to remove clicked suns
    for sun in set(sun_group):
        if dist(pos, sun.get_pos()) <= sun.get_new_dim()[0] / 2 and not sun.is_shrinking():
            sun_sounds()
            sun.make_shrink()
            #sun_group.remove(sun)
            sun_count += sun_value
            return

    # new game button
    if pos[0] >= 895 and pos[1] <= 56:

        reset()
        game_started = False
        day_soundtrack.rewind()
        second_soundtrack.rewind()
        third_soundtrack.rewind()
        day_soundtrack.play()
        sun_count = 50
        score = 0
        wave = 1
        return

    # Find which plant to dig up
    if shovel_selected:
        shovel_selected = False

        if (pos[0] <= LEFT_EDGE_GRID or pos[0] >= RIGHT_EDGE_GRID or
            pos[1] >= BOTTOM_EDGE_GRID or pos[1] <= TOP_EDGE_GRID):
            beep_sounds()
            return

        digging_sounds()
        smallest_dist = 9999
        plant_pos = []
        for grid_pos in create_grid():
            if dist(pos, grid_pos) < smallest_dist:
                smallest_dist = dist(pos, grid_pos)
                plant_pos = grid_pos
        for plant in plant_group:
            if plant.get_pos()[0] == plant_pos[0] and plant.get_pos()[1] == plant_pos[1]:
                plant_group.remove(plant)


    # If shovel is clicked
    elif 815 <= pos[0] <= 890 and pos[1] <= 60:
        shovel_selected = True
        drop_sounds()


    # If plant seed was already selected
    if seed_selected:

        # Increase seed size again
        if plant_image == sunflower_tower_image:
            seed_group[0].change_selection()
        elif plant_image == peashooter_tower_image:
            seed_group[1].change_selection()
        elif plant_image == walnut_tower_image:
            seed_group[2].change_selection()

        # Check if player can afford the plant
        if sun_count - sun_cost < 0 or (pos[0] <= LEFT_EDGE_GRID or pos[0] >= RIGHT_EDGE_GRID or
            pos[1] >= BOTTOM_EDGE_GRID or pos[1] <= TOP_EDGE_GRID):
            beep_sounds()
            seed_selected = False
            return

        # Find the nearest grid location to the click
        smallest_dist = 9999
        plant_pos = []
        for grid_pos in create_grid():
            if dist(pos, grid_pos) < smallest_dist:
                smallest_dist = dist(pos, grid_pos)
                plant_pos = grid_pos

        # Prevents putting plants on top of one another
        for plant in plant_group:
            if plant_pos == plant.get_pos():
                beep_sounds()
                seed_selected = False
                return

        # Plants a new plant
        lane = (plant_pos[1] - first_square[1]) / dist_squares[1]
        health = plant_health
        # If walnut, give more health
        if tower_indicator == 3:
            health *= 4
        new_plant = Plant(sun_cost, plant_image, plant_pos, tower_indicator, lane, health)
        plant_group.add(new_plant)

        drop_sounds()
        sun_count -= sun_cost
        seed_selected = False

    # If plant seed has not been selected
    else:
        if 40 <= pos[0] <= 180:
            clicked = False

            if 80 <= pos[1] <= 180:
                clicked = True
                plant_image = sunflower_tower_image
                tower_indicator = 1
                sun_cost = 50
            elif 210 <= pos[1] <= 310:
                clicked = True
                plant_image = peashooter_tower_image
                tower_indicator = 2
                sun_cost = 100
            elif 330 <= pos[1] <= 440:
                clicked = True
                plant_image = walnut_tower_image
                tower_indicator = 3
                sun_cost = 50

            if clicked:
                digging_sounds()
                seed_selected = True
                seed_group[tower_indicator - 1].change_selection()


# Spawn a new sun on a random part of the grid (sun_timer handler)
def sun_spawner():
    global sun_group
    sun_pos = [random.randrange(LEFT_EDGE_GRID, 880), -50]
    new_sun = Sun(sun_pos, False)
    sun_group.add(new_sun)


# Spawn a sun on top of the sunflowers (sunflower_sun_timer handler)
def sunflower_spawner():
    global sun_group
    for plant in plant_group:
        if plant.get_tower_indicator() == 1:
            sun_group.add(Sun([plant.get_pos()[0], plant.get_pos()[1] + 30], True))


# Spawn peas from the peashooters (pea_timer handler)
def pea_spawner():
    for plant in plant_group:
        if plant.get_tower_indicator() == 2:
            plant.shoot(zombie_group)


# Spawn zombies (zombie_timer handler)
def zombie_spawner():
    global zombie_group
    lane = random.randrange(5)
    zombie_pos = [FRAME_DIM[0], first_square[1] + dist_squares[1] * lane]
    new_zombie = Zombie(zombie_pos, lane, 10)
    zombie_group.add(new_zombie)


# Spawn zombies (zombie_timer handler)
def conehead_spawner():
    global zombie_group
    lane = random.randrange(5)
    zombie_pos = [FRAME_DIM[0], first_square[1] + dist_squares[1] * lane]
    new_zombie = Zombie(zombie_pos, lane, 29)
    zombie_group.add(new_zombie)


# Spawn zombies (zombie_timer handler)
def bucket_spawner():
    global zombie_group
    lane = random.randrange(5)
    zombie_pos = [FRAME_DIM[0], first_square[1] + dist_squares[1] * lane]
    new_zombie = Zombie(zombie_pos, lane, 45)
    zombie_group.add(new_zombie)


# Plays a random zombie groan (zombie_groan_timer handler)
def zombie_groans():
    groan_list = []
    groan_list.append(groan_sound1)
    groan_list.append(groan_sound2)
    groan_list.append(groan_sound3)
    groan_list.append(groan_sound4)
    random.choice(groan_list).play()


def zombie_hits():
    hit_list = []
    hit_list.append(splat_sound1)
    hit_list.append(splat_sound2)
    hit_list.append(splat_sound3)
    hit_list.append(splat_sound4)
    hit_list.append(splat_sound5)
    hit_list.append(splat_sound6)
    hit_list.append(splat_sound7)
    hit_list.append(splat_sound8)
    random.choice(hit_list).play()

def pea_shoot():
    shoot_list = []
    shoot_list.append(shoot_sound1)
    shoot_list.append(shoot_sound2)
    shoot_list.append(shoot_sound3)
    shoot_list.append(shoot_sound4)
    shoot_list.append(shoot_sound5)
    shoot_list.append(shoot_sound6)
    shoot_list.append(shoot_sound7)
    shoot_list.append(shoot_sound8)
    random.choice(shoot_list).play()


def drop_sounds():
    drop_list = []
    drop_list.append(drop_sound1)
    drop_list.append(drop_sound2)
    drop_list.append(drop_sound3)
    drop_list.append(drop_sound4)
    drop_list.append(drop_sound5)
    random.choice(drop_list).play()

def digging_sounds():
    digging_list = []
    digging_list.append(digging_sound1)
    digging_list.append(digging_sound2)
    digging_list.append(digging_sound3)
    digging_list.append(digging_sound4)
    digging_list.append(digging_sound5)
    digging_list.append(digging_sound6)
    digging_list.append(digging_sound7)
    digging_list.append(digging_sound8)
    random.choice(digging_list).play()

def sun_sounds():
    sun_list = []
    sun_list.append(sun_sound1)
    sun_list.append(sun_sound2)
    sun_list.append(sun_sound3)
    sun_list.append(sun_sound4)
    sun_list.append(sun_sound5)
    sun_list.append(sun_sound6)
    sun_list.append(sun_sound7)
    sun_list.append(sun_sound8)
    sun_list.append(sun_sound9)
    sun_list.append(sun_sound10)
    sun_list.append(sun_sound11)
    sun_list.append(sun_sound12)
    random.choice(sun_list).play()

def beep_sounds():
    beep_list = []
    beep_list.append(beep_sound1)
    beep_list.append(beep_sound2)
    beep_list.append(beep_sound3)
    beep_list.append(beep_sound4)
    beep_list.append(beep_sound5)
    random.choice(beep_list).play()

def score35_handler():
    global sun_count, wave, score, seed_selected, shovel_selected, new_wave_flash, new_wave_height
    global not_run_wave2_yet, not_run_wave3_yet

    not_run_wave2_yet = True
    not_run_wave3_yet = True

    sun_count = 500
    wave = 2
    score = 35
    seed_selected = False
    shovel_selected = False
    day_soundtrack.pause()
    third_soundtrack.rewind()

    time = 1000
    time2 = 0
    time3 = 0

    new_wave_flash = True
    new_wave_height = 0


    for sun in set(sun_group):
        sun_group.remove(sun)
    for zombie in set(zombie_group):
        zombie_group.remove(zombie)
    for pea in set(pea_group):
        pea_group.remove(pea)
    for plant in set(plant_group):
        plant_group.remove(plant)

    zombie_timer2.stop()
    conehead_timer2.stop()
    bucket_timer2.stop()

    zombie_timer3.stop()
    conehead_timer3.stop()
    bucket_timer3.stop()

    wave2_zombie_timer.stop()
    wave2_conehead_timer.stop()
    wave2_bucket_timer.stop()

    wave3_zombie_timer.stop()
    wave3_conehead_timer.stop()
    wave3_bucket_timer.stop()

    score_zombie_timer.stop()
    score_conehead_timer.stop()
    score_bucket_timer.stop()


def score80_handler():
    global sun_count, wave, time, time, seed_selected, shovel_selected, new_wave_flash, new_wave_height
    global not_run_wave2_yet, not_run_wave3_yet, score

    not_run_wave2_yet = True
    not_run_wave3_yet = True

    sun_count = 700
    wave = 3
    score = 80
    day_soundtrack.pause()

    seed_selected = False
    shovel_selected = False

    time = 1000
    time2 = 0
    time3 = 0

    new_wave_flash = True
    new_wave_height = 0

    second_soundtrack.rewind()


    for sun in set(sun_group):
        sun_group.remove(sun)
    for zombie in set(zombie_group):
        zombie_group.remove(zombie)
    for pea in set(pea_group):
        pea_group.remove(pea)
    for plant in set(plant_group):
        plant_group.remove(plant)

    zombie_timer2.stop()
    conehead_timer2.stop()
    bucket_timer2.stop()

    zombie_timer3.stop()
    conehead_timer3.stop()
    bucket_timer3.stop()
    ###

    wave2_zombie_timer.stop()
    wave2_conehead_timer.stop()
    wave2_bucket_timer.stop()

    wave3_zombie_timer.stop()
    wave3_conehead_timer.stop()
    wave3_bucket_timer.stop()

    score_zombie_timer.stop()
    score_conehead_timer.stop()
    score_bucket_timer.stop()


#################################################################################################################
# DRAWING AND COLLISIONS #



# Process group of sprites
def draw_group(canvas, group):
    for element in set(group):
        element.draw(canvas)


# Detect pea/zombie collisions
def pea_zombie_collide():
    global score, zombie_vel, wave, time, new_wave_flash, new_wave_height, sun_count
    zombie_remove_group = set([])
    pea_remove_group = set([])

    for zombie in set(zombie_group):
        for pea in set(pea_group):

            # Pea hit a zombie
            if pea.collide(zombie):
                zombie.pea_hit()
                zombie_hits()
                #splat_sound.play()
                pea_remove_group.add(pea)
                # If zombie dies
                if zombie.get_health() <= 0:
                    zombie_remove_group.add(zombie)
                    score += 1
                    zombie_vel += 0.005
                    # If the next wave is reached
                    if score == wave1_cap or score == wave2_cap:
                        reset()
                        new_wave_flash = True
                        new_wave_height = 0
                        time = 1000
                        day_soundtrack.pause()
                        second_soundtrack.pause()
                        if score == wave1_cap:
                            wave = 2
                            second_soundtrack.play()
                            if sun_count < 400:
                                sun_count = 400
                        elif score == wave2_cap:
                            wave = 3
                            third_soundtrack.play()
                            if sun_count < 500:
                                sun_count = 500
                        return

    # Remove the necessary peas and zombies
    for zombie in zombie_remove_group:
        zombie_group.remove(zombie)
    for pea in pea_remove_group:
        pea_group.remove(pea)


# Detect plant/zombie collisions
def plant_zombie_collide(zombie):
    for plant in set(plant_group):
        if plant.collide(zombie):
            plant.hit(zombie)
            eating_sound.play()
            if plant.get_health() <= 0:
                plant_group.remove(plant)
            return True


# Handler to draw on canvas (60 times per second)
def draw(canvas):
    global highscore, time, time2, time3, game_started, sun_count, score, wave, new_wave_height
    global not_run_wave2_yet, not_run_wave3_yet, not_run_150_yet

    #TODOVDNAKSDNVKADSVANDKVLANDSV
    #if time == 1:
        #zombie_spawner()
        #conehead_spawner()
        #bucket_spawner()

    if game_started:
        time += 1
        # Spawns more zombies as time goes along
        if time > 5400:
            zombie_timer2.start()
            conehead_timer2.start()
            bucket_timer2.start()
        if time > 10800:
            zombie_timer3.start()
            conehead_timer3.start()
            bucket_timer3.start()

        # Replay soundtrack
        if time % 9000 and wave == 1:
            day_soundtrack.play()


    if wave == 2:
        time2 += 1
        if time2 % 7000:
            second_soundtrack.play()
    if wave == 3:
        time3 += 1
        if time3 % 9400:
            third_soundtrack.play()

    if wave == 2 and not_run_wave2_yet:
        not_run_wave2_yet = False
        wave2_zombie_timer.start()
        wave2_conehead_timer.start()
        wave2_bucket_timer.start()

    if wave == 3 and not_run_wave3_yet:
        not_run_wave3_yet = False
        wave3_zombie_timer.start()
        wave3_conehead_timer.start()
        wave3_bucket_timer.start()

    if score == 120 and not_run_150_yet:
        not_run_150_yet = False
        score_zombie_timer.start()
        score_conehead_timer.start()
        score_bucket_timer.start()

    if not zombie_group:
        for plant in plant_group:
            plant.not_being_hit()

    # Draw the background
    canvas.draw_image(day_background_image, day_background_info.get_center(), day_background_info.get_size(),
                      day_background_info.get_center(), day_background_info.get_size())

    # Draw the menu if the game hasn't started
    if not game_started:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(),
                          [FRAME_DIM[0] / 2, FRAME_DIM[1] / 3], desired_splash_dim)
        canvas.draw_image(play_image, button_info.get_center(), button_info.get_size(),
                          [400, 410], desired_button_dim)
        canvas.draw_image(howtoplay_image, button_info.get_center(), button_info.get_size(),
                          [500, 410], desired_button_dim)
        canvas.draw_image(highscore_image, [77, 77], [154, 154],
                          [600, 410], desired_button_dim)
        if show_instr:
            canvas.draw_image(instructions_image, instructions_info.get_center(), instructions_info.get_size(),
                              [FRAME_DIM[0] / 2, FRAME_DIM[1] / 2], desired_instr_dim)
        if show_score:
            canvas.draw_image(highscore_back_image, instructions_info.get_center(), instructions_info.get_size(),
                              [FRAME_DIM[0] / 2, FRAME_DIM[1] / 2], desired_instr_dim)
            canvas.draw_text(str(highscore), [641, 295], 50, 'White', 'monospace')
        return

    sun_timer.start()
    #pea_timer.start()
    zombie_timer.start()
    conehead_timer.start()
    bucket_timer.start()
    zombie_groan_timer.start()
    #sunflower_sun_timer.start()

    # Draw wave count in top left corner
    canvas.draw_image(wave_image, wave_info.get_center(), wave_info.get_size(),
                      [60, 30], desired_wave_dim)
    canvas.draw_text(str(wave), [90, 45], 40, "White", 'monospace')

    # Draw sun and score in bottom right corner
    canvas.draw_image(sunscore_image, sunscore_info.get_center(), sunscore_info.get_size(),
                      [850, 600], desired_sunscore_dim)
    canvas.draw_text(str(sun_count), [770, 614], 40, 'White', 'monospace')
    canvas.draw_text(str(score), [940, 614], 40, 'White', 'monospace')

    # Draw seed packets
    counter = 1
    for seed in seed_group:
        seed.draw(canvas, [first_seed_pos[0], first_seed_pos[1] * counter])
        counter += 1

    # new game button
    canvas.draw_image(newgame_image, [170, 92], [340, 184], [960, 30], [130, 60])

    # shovel button
    if shovel_selected:
        canvas.draw_image(shovel_image, [69, 70], [139, 141], [850, 30], [40, 30])
    else:
        canvas.draw_image(shovel_image, [69, 70], [139, 141], [850, 30], [80, 60])

    # Draw the planted plants on the grid
    draw_group(canvas, plant_group)

    # Draw zombies and detect if collision with a plant
    for zombie in zombie_group:
        zombie.draw(canvas)
        if not plant_zombie_collide(zombie):
            zombie.update()

    # Draw the suns on the grid
    draw_group(canvas, sun_group)

    # Draw the peas on the grid
    for pea in pea_group:
        pea.draw(canvas)
        canvas.draw_image(peashadow_image, [265, 114], [529, 227], [pea.get_pos()[0], pea.get_pos()[1] + 50], desired_pea_dim)
        pea.update()



    # Detect collisions between peas and zombies
    pea_zombie_collide()

    if new_wave_flash:
        canvas.draw_text("NEW WAVE!", [FRAME_DIM[0] / 2, new_wave_height], 50, "White", "monospace")
        new_wave_height += 1

    # Detect game overs
    for zombie in zombie_group:
        if zombie.get_pos()[0] < game_over_line:
            reset()
            gameover_sound.play()
            game_started = False
            day_soundtrack.rewind()
            second_soundtrack.rewind()
            third_soundtrack.rewind()
            day_soundtrack.play()
            sun_count = 50
            score = 0
            wave = 1
            highscore = score

            zombie_timer2.stop()
            conehead_timer2.stop()
            bucket_timer2.stop()

            zombie_timer3.stop()
            conehead_timer3.stop()
            bucket_timer3.stop()



#################################################################################################################



# Initialize stuff
sun_group = set([])
plant_group = set([])
pea_group = set([])
zombie_group = set([])
seed_group = []
add_seeds()

sun_timer = simplegui.create_timer(sun_spawn_freq, sun_spawner)
pea_timer = simplegui.create_timer(pea_shoot_freq, pea_spawner)
sunflower_sun_timer = simplegui.create_timer(sunflower_spawn_freq, sunflower_spawner)

zombie_timer = simplegui.create_timer(zombie_spawn_freq, zombie_spawner)
zombie_timer2 = simplegui.create_timer(zombie_spawn_freq, zombie_spawner)
zombie_timer3 = simplegui.create_timer(zombie_spawn_freq, zombie_spawner)

wave2_zombie_timer = simplegui.create_timer(zombie_spawn_freq * 1.5, zombie_spawner)
wave2_conehead_timer = simplegui.create_timer(conehead_spawn_freq * 1.5, conehead_spawner)
wave2_bucket_timer = simplegui.create_timer(bucket_spawn_freq * 1.5, bucket_spawner)

wave3_zombie_timer = simplegui.create_timer(zombie_spawn_freq * 4, zombie_spawner)
wave3_conehead_timer = simplegui.create_timer(conehead_spawn_freq * 4, conehead_spawner)
wave3_bucket_timer = simplegui.create_timer(bucket_spawn_freq * 4, bucket_spawner)

score_zombie_timer = simplegui.create_timer(zombie_spawn_freq, zombie_spawner)
score_conehead_timer = simplegui.create_timer(conehead_spawn_freq, conehead_spawner)
score_bucket_timer = simplegui.create_timer(bucket_spawn_freq, bucket_spawner)

conehead_timer = simplegui.create_timer(conehead_spawn_freq, conehead_spawner)
conehead_timer2 = simplegui.create_timer(conehead_spawn_freq, conehead_spawner)
conehead_timer3 = simplegui.create_timer(conehead_spawn_freq, conehead_spawner)

bucket_timer = simplegui.create_timer(bucket_spawn_freq, bucket_spawner)
bucket_timer2 = simplegui.create_timer(bucket_spawn_freq, bucket_spawner)
bucket_timer3 = simplegui.create_timer(bucket_spawn_freq, bucket_spawner)

zombie_groan_timer = simplegui.create_timer(zombie_groan_freq, zombie_groans)


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Plants vs. Zombies", FRAME_DIM[0], FRAME_DIM[1])

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick_handler)
button1 = frame.add_button('Skip to Wave 2 (score = 35)', score35_handler)
button2 = frame.add_button('Skip to Wave 3 (score = 80)', score80_handler)

# Start the frame animation
frame.start()
day_soundtrack.play()
