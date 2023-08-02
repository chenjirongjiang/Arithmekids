"""This is the file that contains all the credits."""
import copy

credit_order = [
    True, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    ]

credit_order_copy = [
    True, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    ]

message = ["", "Speed up the credits", "by pressing space", "", "Slow them down", "by pressing backspace"]
message_coor = [650, 700, 740, 780, 820, 860] # Coordinate on y-axis
message_x = [300, 300, 300, 300, 300, 300] # Coordinate on x-axis

directors = ["Game directors", "Siem Jongsma", "Chen Ji Rong 'Jack' Jiang", "Nikki Rademaker", "Amarise Silié", "Yanna Smid"]
d_coordinates = [650, 700, 740, 780, 820, 860]
d_x = [300, 300, 300, 300, 300, 300]

supervisors = ["Supervisors", "Giulio Barbero", "Fenia Aivaloglou", " ", " ", " "]
s_coordinates = [650, 700, 750, 800, 800, 900]
s_x = [300, 300, 300, 300, 300, 300]

designers = ["Game designers", "Siem Jongsma", "Chen Ji Rong 'Jack' Jiang", "Nikki Rademaker", "Amarise Silié", "Yanna Smid"]
des_coordinates = [650, 700, 750, 800, 850, 900]
des_x = [270, 270, 270, 270, 270, 270]

music = ["Background music", "Main screens: cute", "Field: smile", "Beach: ukelele", "Sea: psychedelic", ""]
music_coor = [650, 750, 850, 950, 1050, 1040]
music_x = [300, 300, 300, 300, 300, 300]

music_2 = ["", "Snow: littleidea", "Space: enigmatic", "Credit: adventure", "from Bensound.com", ""]
music_coor_2 = [620, 750, 850, 950, 1050, 1060]
music_x_2 = [300, 300, 300, 300, 300, 300]

music_program = ["Music programming", "Nikki Rademaker", "", "", "", ""]
m_pr_coor = [650, 700, 730, 730, 730, 750]
m_pr_x = [250, 290, 300, 300, 300, 300]

bg_program = ["Background programming", "Chen Ji Rong 'Jack' Jiang", "Yanna Smid", "Nikki Rademaker", "", ""]
bg_pr_coordinates = [650, 700, 740, 800, 850, 900]
bg_pr_x = [200, 300, 300, 300, 300, 300]

text_program = ["Text programming", "Amarise Silié", "Siem Jongsma", "Yanna Smid", "Chen Ji Rong 'Jack' Jiang", "Nikki Rademaker"]
text_coor = [650, 700, 750, 800, 850, 900]
text_x = [245, 300, 300, 300, 300, 300]

level_program = ["Level programming", "Amarise Silié", "Yanna Smid", "Siem Jongsma", "Chen Ji Rong 'Jack' Jiang", ""]
l_pr_coor = [650, 700, 750, 800, 850, 900]
l_pr_x_ = [235, 300, 300, 300, 300, 300]

multi_program = ["Multiplayer programming", "Yanna Smid", "Nikki Rademaker", "Chen Ji Rong 'Jack' Jiang", "", "", ""]
multi_coor = [650, 700, 750, 800, 850, 900]
multi_x = [210, 300, 300, 300, 300, 300]

timer_program = ["Time Attack programming", "Siem Jongsma", "Amarise Silié", "", "", ""]
time_coor= [650, 700, 750, 800, 850, 900]
time_x = [210, 300, 300, 300, 300, 300]

button_program = ["Button programming", "Nikki Rademaker", "", "", "", ""]
b_pr_coor = [650, 700, 750, 800, 850, 900]
b_pr_x = [235, 300, 300, 300, 300, 300]

credit_program = ["Credit programming", "Yanna Smid", "Amarise Silié", "", "", ""]
cred_coor = [650, 700, 750, 800, 850, 900]
cred_x = [240, 300, 300, 300, 300, 300]

bg_design = ["Background designs", "Yanna Smid", "Nikki Rademaker", " ", " ", " "]
bg_coordinates = [650, 700, 750, 800, 850, 900]
bg_x = [220, 300, 300, 300, 300, 300]

button_design = ["Button designs", "Nikki Rademaker", "Yanna Smid", " ", " ", " "]
b_coordinates = [650, 700, 750, 800, 850, 900]
b_x = [280, 300, 300, 300, 300, 300]

char_design = ["Character designs", "Yanna Smid", "Nikki Rademaker", "", "", ""]
char_coor = [650, 700, 750, 800, 850, 900]
char_x = [270, 300, 300, 300, 300, 300]

char_actors = ["Actors", "LEAD: Bee", "Monkey", "Penguin", "Nikkelien the Alien", ""]
actors_coor = [650, 700, 750, 800, 850, 910]
actors_x = [300, 300, 300, 300, 300, 300]

producers = ["Produced by", "Siem Jongsma", "Chen Ji Rong 'Jack' Jiang", "Nikki Rademaker", "Amarise Silié", "Yanna Smid"]
prod_coor = [650, 700, 750, 800, 850, 900]
prod_x = [300, 300, 300, 300, 300, 300]

developers = ["Developed by", "Siem Jongsma", "Chen Ji Rong 'Jack' Jiang", "Nikki Rademaker", "Amarise Silié", "Yanna Smid"]
dev_coor = [650, 700, 750, 800, 850, 900]
dev_x = [300, 300, 300, 300, 300, 300]

last_creds = ["Leiden University", "Faculty of Science", "Bioinformatics", "", "", ""]
last_coor = [650, 700, 750, 800, 850, 900]
last_x = [270, 270, 270, 300, 300, 300]

special_thanks = ["Special thanks to", "Ourselves", "", "Friends and family", "who tested our program", ""]
special_coor = [650, 700, 750, 800, 850, 900]
special_x = [230, 230, 230, 230, 230, 300]

thanks = ["Thanks for playing!", "", "Stay for the trivia!", "", "", ""]
thanks_coor = [650, 700, 750, 800, 850, 900]
thanks_x = [230, 300, 260, 300, 300, 300]

trivia_1 = ["Sea", "is the world that took", "the longest to draw", "", "", ""]
trivia_1_coor = [650, 700, 750, 800, 850, 900]
trivia_1_x = [300, 300, 300, 300, 300, 300]

trivia_2 = ["Level 25", "is the hardest to", "complete for the", "game makers", "", ""]
trivia_2_coor = [650, 700, 750, 800, 850, 900]
trivia_2_x = [300, 300, 300, 300, 300, 300]

trivia_3 = ["Timer high scores", "from the game makers", "easy: 48 by Amarise", "medium: 43 by Amarise", "hard: 35 by Yanna", ""]
trivia_3_coor = [650, 700, 750, 800, 850, 900]
trivia_3_x = [240, 300, 300, 300, 300, 300]

trivia_4 = ["Favorite worlds", "Siem: Beach", "Jack: Space", "Nikki: Beach", "Amarise: Sea", "Yanna: Snow"]
trivia_4_coor = [650, 700, 750, 800, 850, 900]
trivia_4_x = [300, 300, 300, 300, 300, 300]

all_credits = [
    message, directors, supervisors, designers, music, music_2, music_program, bg_program,
    text_program, level_program, multi_program, timer_program, button_program, credit_program,
    bg_design, button_design, char_design, char_actors, producers, developers, last_creds,
    special_thanks, thanks, trivia_1, trivia_2, trivia_3, trivia_4,
    ]

all_coordinates = [
    message_coor, d_coordinates, s_coordinates, des_coordinates, music_coor, music_coor_2,
    m_pr_coor, bg_pr_coordinates, text_coor, l_pr_coor, multi_coor, time_coor, b_pr_coor,
    cred_coor, bg_coordinates, b_coordinates, char_coor, actors_coor, prod_coor, dev_coor,
    last_coor, special_coor, thanks_coor, trivia_1_coor, trivia_2_coor, trivia_3_coor,
    trivia_4_coor,
    ]
all_coordinates_copy = copy.deepcopy(all_coordinates)

all_x_coordinates = [
    message_x, d_x, s_x, des_x, music_x, music_x_2, m_pr_x, bg_pr_x, text_x, l_pr_x_,
    multi_x, time_x, b_pr_x, cred_x, bg_x, b_x, char_x, actors_x, prod_x, dev_x, last_x,
    special_x, thanks_x, trivia_1_x, trivia_2_x, trivia_3_x, trivia_4_x,
    ]
