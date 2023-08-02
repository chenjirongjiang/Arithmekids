"""This is the file with background settings."""
import pygame

class Background:
    """Initialize background (settings)."""

    def __init__(self, folder, name):
        """Initialize background (settings)."""
        self.name = name
        self.screen = pygame.display.set_mode((800, 600))
        self.path = folder +"/"+ self.name + ".png"

    def bg(self, canvas): #canvas being "transparant" or "white"
        """Converts the images depending on the canvas.
        
        Parameters:
        canvas: string that defines the type of canvas the image will 
                be on, this can be 'white' or 'transparant'

        Return: converted version of the image
        """
        if canvas == "white":
            surface = pygame.image.load(self.path).convert()
        elif canvas == "transparant" :
            surface = pygame.image.load(self.path).convert_alpha()
        return surface

# Buttons
home_button = pygame.image.load('buttons/home_b.png')
home_button = pygame.transform.scale(home_button, (89, 89))
menu_button_1 = pygame.image.load('buttons/multi_b.png')
menu_button_2 = pygame.image.load('buttons/levels_b.png')
menu_button_3 = pygame.image.load('buttons/timer_b.png')
clear_image = pygame.image.load('images/trashcan.PNG')
clear_image = pygame.transform.scale(clear_image, (54, 88))
small_menu_button_3 = pygame.transform.scale(menu_button_3, (89, 89))
levelmap_b = pygame.image.load('buttons/levelmap_b.png')
levelmap_b = pygame.transform.scale(levelmap_b, (107, 107))

field_button = pygame.image.load('buttons/fieldworld_b.png')
field_button = pygame.transform.scale(field_button, (110, 110))
beach_button = pygame.image.load('buttons/beachworld_b.png')
beach_button = pygame.transform.scale(beach_button, (110, 110))
beach_lock = pygame.image.load('buttons/beachworld_b_lock.png')
beach_lock = pygame.transform.scale(beach_lock, (110, 110))
sea_button = pygame.image.load('buttons/seaworld_b.png')
sea_button = pygame.transform.scale(sea_button, (110, 110))
sea_lock = pygame.image.load('buttons/seaworld_b_lock.png')
sea_lock = pygame.transform.scale(sea_lock, (110, 110))
snow_button = pygame.image.load('buttons/snowworld_b.png')
snow_button = pygame.transform.scale(snow_button, (110, 110))
snow_lock = pygame.image.load('buttons/snowworld_b_lock.png')
snow_lock = pygame.transform.scale(snow_lock, (110, 110))
space_button = pygame.image.load('buttons/space_b.png')
space_button = pygame.transform.scale(space_button, (110, 110))
space_lock = pygame.image.load('buttons/space_b_lock.png')
space_lock = pygame.transform.scale(space_lock, (110, 110))

easy_button = pygame.image.load('buttons/timer_easy_b.png')
easy_button = pygame.transform.scale(easy_button, (155, 155))
medium_button = pygame.image.load('buttons/timer_medium_b.png')
medium_button = pygame.transform.scale(medium_button, (155, 155))
hard_button = pygame.image.load('buttons/timer_hard_b.png')
hard_button = pygame.transform.scale(hard_button, (155, 155))

# Multiplayer images
red_heart = pygame.image.load("images/RED_heart.png")
p_1_heart = pygame.transform.scale(red_heart, (40, 40))
blue_heart = pygame.image.load("images/blue_heart.png")
p_2_heart = pygame.transform.scale(blue_heart, (40, 40))

# Field images
bg_field = Background("field_bg", "bg_with_house").bg("white")
pre_cloud1 = Background("field_bg", "cloud1").bg("transparant")
cloud1 = pygame.transform.scale(pre_cloud1, (300, 180))
pre_cloud2 = Background("field_bg", "cloud2").bg("transparant")
cloud2 = pygame.transform.scale(pre_cloud2, (300, 180))
pre_cloud3 = Background("field_bg", "cloud3").bg("transparant")
cloud3 = pygame.transform.scale(pre_cloud3, (300, 180))
pre_bee = Background("field_bg", "bee").bg("transparant")
bee = pygame.transform.scale(pre_bee, (300, 290))

# List containing field bg images, order is enforced
fieldworld_bg = [bg_field, cloud1, cloud2, cloud3, bee]
field_coordinates = [[0, 0], [300, 120], [500, 50], [500, 400]]
field_speed_x = [0.18, 0.25, 0.2, 0.5] # Image moving speed on x-axis
field_speed_y = [0, 0, 0, 0] # Image moving speed on y-axis

# Beach images
bg_beach = Background("beach_bg", "bg_beachworld").bg("white")
pre_airplane = Background("beach_bg", "airplane").bg("transparant")
airplane = pygame.transform.scale(pre_airplane, (246, 185))
pre_bee_bw = Background("beach_bg", "bee_beach").bg("transparant")
bee_bw = pygame.transform.scale(pre_bee_bw, (305, 225))
bg_beachworld = [bg_beach, airplane, cloud2, bee_bw, bee_bw]
beach_coordinates = [[700, 60], [300, 10], [-1000, 0], [500, 400]]
beach_speed_x = [-0.7, 0.25, 0, 0.5]
beach_speed_y = [0, 0, 0, 0]

# Sea images
bg_sea = Background("sea_bg", "bg_seaworld").bg("white")
pre_o_fish = Background("sea_bg", "orange_fish").bg("transparant")
o_fish = pygame.transform.scale(pre_o_fish, (300, 180))
pre_y_fish = Background("sea_bg", "yellow_fish").bg("transparant")
y_fish = pygame.transform.scale(pre_y_fish, (400, 240))
pre_shark = Background("sea_bg", "shark").bg("transparant")
shark = pygame.transform.scale(pre_shark, (300, 180))
pre_bee_sw = Background("sea_bg", "bij_seaworld").bg("transparant")
bee_sw = pygame.transform.scale(pre_bee_sw, (400, 350))
bg_seaworld = [bg_sea, o_fish, y_fish, shark, bee_sw]
sea_coordinates = [[10, 100], [0, 120], [550, 50], [500, 400]]
sea_speed_x = [-0.55, -0.55, 0.8, 0.3]
sea_speed_y = [0, 0, 0, 0]

# Snow images
bg_snow = Background("snow_bg", "bg_snowworld").bg("white")
pre_penguin = Background("snow_bg", "penguin").bg("transparant")
penguin = pygame.transform.scale(pre_penguin, (239, 179))
pre_snowflake = Background("snow_bg", "snowflake").bg("transparant")
snowflake = pygame.transform.scale(pre_snowflake, (366, 216))
pre_bee_snow = Background("snow_bg", "snow_bee").bg("transparant")
bee_snow = pygame.transform.scale(pre_bee_snow, (162, 121))
bg_snowworld = [bg_snow, penguin, snowflake, snowflake, bee_snow]
snow_coordinates = [[700, 450], [-100, 0], [500, 0], [500, 90]]
snow_speed_x = [-1, 0, 0, 0.5]
snow_speed_y = [0, 0.2, 0.3, 0]

# Space images
bg_space = Background("space_bg", "bg_space").bg("white")
pre_rocket = Background("space_bg", "rocket").bg("transparant")
rocket = pygame.transform.scale(pre_rocket,(333, 190))
bee_space = Background("space_bg", "space_bee").bg("transparant")
bg_spaceworld = [bg_space, bee_space, rocket, bee_space, bee_space]
space_coordinates = [[1000, 0], [300, 400], [1000, 0], [600, 100]]
space_speed_x = [0, 0.7, 0, 0]
space_speed_y = [0, 0, 0, 0.3]

bg_credit_screen = Background("credit_bg", "bg_credit_screen").bg("white")
pre_cloud1_cs = Background("credit_bg", "cloud1").bg("transparant")
cloud1_cs = pygame.transform.scale(pre_cloud1_cs, (300, 180))
pre_cloud2_cs = Background("credit_bg", "cloud2").bg("transparant")
cloud2_cs = pygame.transform.scale(pre_cloud2_cs, (300, 180))
pre_cloud3_cs = Background("credit_bg", "cloud3").bg("transparant")
cloud3_cs = pygame.transform.scale(pre_cloud3_cs, (300, 180))
pre_sleeping_bee = Background("credit_bg", "sleeping_bee").bg("transparant")
sleeping_bee = pygame.transform.scale(pre_sleeping_bee, (300, 250))

# Credits
# List containing bg images, order is enforced
credits_bg = [bg_credit_screen, cloud2_cs, cloud1_cs, cloud3_cs, sleeping_bee]
credits_coordinates = [[300, 70], [500, 50], [0, 0], [500, 400]]
credits_speed_x = [0.18, 0.25, 0.2, 0.5]
credits_speed_y = [0, 0, 0, 0]
