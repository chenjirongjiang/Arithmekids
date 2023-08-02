"""This is the main game file."""
import sys
import random
import operator
import pygame
import credit as creds
from music import *
from background import *
from levels import levels
import shelve
import os

class Game:
    """Overall class to manage the game."""

    def __init__(self, text = '', user_input = '', name = ''):
        """Initialize the game and screen."""
        pygame.init()
        pygame.mixer.init() # Initialize module: makes sure music can be loaded and played
        self.my_font = pygame.font.Font(None, 70)
        self.screen = pygame.display.set_mode((800, 600))
        self.name = name
        self.text = text
        self.text_surface = self.my_font.render(self.text, True, (0, 0, 0))
        self.user_input = user_input

        self.input_box = pygame.Rect(460, 248, 190, 50)

        self.music_button = self.screen.blit(sound_button, (720, 530))
        self.sound = True
        self.music_play = False

        self.level = 1
        self.difficulty = None
        self.first_unlock = False
        #self.worlds_unlocked = [True, False, False, False, False]
        self.worlds_unlocked = [True, True, True, True, True]

        
        self.shelf_file = shelve.open('save_file/save_file')
        self.shelf_file['world_beach'] = self.worlds_unlocked[1]
        self.shelf_file['world_sea'] = self.worlds_unlocked[2]
        self.shelf_file['world_snow'] = self.worlds_unlocked[3]
        self.shelf_file['world_space'] = self.worlds_unlocked[4]
        self.shelf_file.close()

        self.credit_number = 0
        self.next_credit = 1

        self.clock = pygame.time.Clock()
        self.bg_color = (163, 199, 255)
        pygame.display.set_caption("Arithmekids")

    def mute(self, music_world):
        """Makes sure that the music doesn't start playing when you go to a
        different page after the mute button is pressed. Also makes sure
        that the song doesn't restart when going back to the menu.

        Parameter:
        music_world: the song that should be played

        Returns: song starts playing or song is not playing
            """
        if self.sound:
            # Plays different songs in different windows
            self.music_play = True
            return music(music_world)
        else:
            # Song stops playing when going to different window if mute button is pressed
            self.music_play = False
            return pygame.mixer.music.stop()

    def mute_button(self):
        """Changes button depending on whether the music is muted or not.
        If music is playing, mute button gets displayed.
        If music has stopped, unmute button gets displayed.
        """
        if self.sound:
            self.music_button = self.screen.blit(sound_button, (720, 530))
        else:
            self.music_button = self.screen.blit(no_sound_button, (720, 530))

    def my_print(self, output, x_pos, y_pos, color=(0,0,0), size=30):
        """Displays exercises on screen.

        Parameters:
        output: str with text that will be printed onto the screen
        x_pos: int with x-coordinate of output
        y_pos: int with y-coordinate of output
        color: tuple containing ints with rgb color code of output
        size: int with font size of output
        """
        self.my_font = pygame.font.Font(None, size)
        my_text = self.my_font.render(output, True, color)
        self.screen.blit(my_text, (x_pos, y_pos))

    def print_question(self, print_this, position, color=(0,0,0), size=70):
        """Prints the question, position depends on length of output.
        Can be used for all modes.

        Parameters:
        print_this: str with exercise that will be printed onto the screen
        position: tuple of x and y-coordinates of print_this
        color: tuple containing ints with rgb color code of print_this
        size: int with font size of print_this
        """
        if len(print_this) == 9:
            self.my_print(print_this, position[0]-20, position[1], color, size)
        elif len(print_this) > 9:
            self.my_print(print_this, position[0]-50, position[1], color, size)
        else:
            self.my_print(print_this, position[0], position[1], color, size)

    def handle_input(self, event, color=(0,0,0)):
        """Handles the user input depending on the pressed keyboard key.

        Parameters:
        event: action that is executed
        color: tuple containing ints with rgb color code of text
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.user_input = self.text
                self.text = ''
            else:
                if len(self.text) < 5:
                    num = [
                        pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                        pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
                        ]
                    if event.key in num:
                        self.text += event.unicode
            self.text_surface = self.my_font.render(self.text, True, color)

    def name_choice(self, event):
        """Players from multiplayer mode can choose their own name."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.name = self.text
                self.text = ''
            else:
                if len(self.text) < 10:
                    if event.key == pygame.K_SPACE:
                        self.text += ""
                    else:
                        self.text += event.unicode
            self.text_surface = self.my_font.render(self.text, True, (0, 0, 0))

    def input_box_set(self, width=37, color=(0,0,0)):
        """Contains input box settings.

        Parameters:
        width: int with width of input box
        color: tuple containing ints with rgb color code of text
        """
        self.screen.blit(self.text_surface, (self.input_box.x+5, self.input_box.y+5))
        pygame.draw.rect(self.screen, color, self.input_box, 2)
        self.input_box.w = max(width, self.text_surface.get_width() + 10)

    def check_answer(self, right_answer, question, user_answer, score, mistakes):
        """Compares the right answer with the user input. If the user input is correct,
        the user's score is increased by 1. If it is incorrect, the question will be
        repeated later on.

        Parameters:
        right_answer: str with the correct answer to the current question
        question: tuple with the chosen integers and operator
        user_answer: str with the input answer of the user
        score: int with the current score of the user
        mistakes: list with the questions the user answered incorrectly

        Returns: tuple with evaluation string, score and mistakes
        """
        # If the correct answer is given, the score is increased by 1
        if right_answer == user_answer:
            if question in mistakes:
                mistakes.remove(question)
            self.user_input = ''
            score += 1
            return ("That is correct!", score, mistakes)

        # If the wrong answer is given, the question is added to mistakes
        else:
            self.user_input = ''
            if question not in mistakes:
                mistakes.append(question)
            return ("Sorry, we will try that one again later", score, mistakes)

    def repeat_mistakes(self, already_done, one_question, mistakes):
        """Repeats the exercises that the user got wrong.

        Parameters:
        already_done: list with the questions that have already been displayed
        one_question: bool that is set to True when a question has been made,
            and set to False when a new question needs to be generated
        mistakes: list with the questions the user answered incorrectly

        Returns:
        tuple with one_question, already_done, the generated question,
            and the correct answer to the generated question
        """
        operators = {"+": operator.add, "-": operator.sub, "×": operator.mul, ":": operator.truediv}

        # A random question is chosen from the mistakes
        question = random.choice(mistakes)
        question_operator = operators.get(question[2])
        right_answer = str(int(question_operator(question[0], question[1])))
        one_question = True
        return (one_question, already_done, question, right_answer)

    def moving_bg(self, background_theme, coordinates, x_movement, y_movement):
        """Contains settings for moving field background items."""
        # Background
        self.screen.blit(background_theme[0], (0,0))

        # Moving images
        coordinates[0][0] += x_movement[0] # x-coordinate of im1
        if coordinates[0][0] >= 900:
            coordinates[0][0] = -250
        elif coordinates[0][0] < -270:
            coordinates[0][0] = 900
        coordinates[0][1] += y_movement[0]
        if coordinates[0][1] >= 700:
            coordinates[0][1] = -100
        self.screen.blit(background_theme[1], (round(coordinates[0][0]), round(coordinates[0][1])))

        coordinates[1][0] += x_movement[1] # x-coordinate of im2
        if coordinates[1][0] >= 800:
            coordinates[1][0] = -250
        elif coordinates[1][0] < -250:
            coordinates[1][0] = 799

        coordinates[1][1] += y_movement[1] #y coordinaat im2
        if coordinates[1][1] >= 700:
            coordinates[1][1] = -100
        self.screen.blit(background_theme[2], (round(coordinates[1][0]), round(coordinates[1][1])))

        coordinates[2][0] += x_movement[2] #<-- x coordinaat im3
        if coordinates[2][0] >= 800:
            coordinates[2][0] = -250
        elif coordinates[2][0] < -250:
            coordinates[2][0] = 799

        coordinates[2][1] += y_movement[2] #<-- y coordinaat im3
        if coordinates[2][1] >= 700:
            coordinates[2][1] = -100
        self.screen.blit(background_theme[3], (round(coordinates[2][0]), round(coordinates[2][1])))

        coordinates[3][0] -= x_movement[3] #<--x coordinaat van bee
        if coordinates[2][0] >= 800:
            coordinates[2][0] = -250
        elif coordinates[3][0] < -250:
            coordinates[3][0] = 799
        # self.screen.blit(background_theme[4], (round(self.bee_x_pos), self.bee_y_pos))

        coordinates[3][1] += y_movement[3] #<-- y coordinaat van bee
        if background_theme[4] == bee_space:
            if coordinates[3][1] > 145:
                y_movement[3] = y_movement[3] * -1
            if coordinates[3][1] < 40:
                y_movement[3] = y_movement[3] * -1
        else:
            if coordinates[3][1] >= 700:
                coordinates[3][1] = -100
        self.screen.blit(background_theme[4], (round(coordinates[3][0]), round(coordinates[3][1])))

    def multiplayer_lives(self, p_1_heart, p_2_heart, p_1_lives, p_2_lives):
        """Keeps track of the lives."""
        if p_1_lives == 3:
            self.screen.blit(p_1_heart, (20, 90))
            self.screen.blit(p_1_heart, (60, 90))
            self.screen.blit(p_1_heart, (100, 90))
        elif p_1_lives == 2:
            self.screen.blit(p_1_heart, (20, 90))
            self.screen.blit(p_1_heart, (60, 90))
        elif p_1_lives == 1:
            self.screen.blit(p_1_heart, (20, 90))
        elif p_1_lives == 0:
            p_1_lives = 0
        if p_2_lives == 3:
            self.screen.blit(p_2_heart, (500, 90))
            self.screen.blit(p_2_heart, (540, 90))
            self.screen.blit(p_2_heart, (580, 90))
        elif p_2_lives == 2:
            self.screen.blit(p_2_heart, (500, 90))
            self.screen.blit(p_2_heart, (540, 90))
        elif p_2_lives == 1:
            self.screen.blit(p_2_heart, (500, 90))
        elif p_2_lives == 0:
            p_2_lives = 0

    def run_game(self):
        """This is the loop so the game can run."""
        one_question = False
        score, count = 0, 0
        already_done, mistakes = [], []
        evaluate, congratulations = False, False

        evaluatetimerevent = pygame.USEREVENT + 1
        congratulationstimerevent = pygame.USEREVENT + 2
        chosen_levels = levels[self.level-1:self.level+4]

        # Every world has its own song
        if self.level >= 1 and self.level < 6:
            self.mute(music_field_world)
        elif self.level >= 6 and self.level < 11:
            self.mute(music_beach)
        elif self.level >= 11 and self.level < 16:
            self.mute(music_sea)
        elif self.level >= 16 and self.level < 21:
            self.mute(music_snow)
        elif self.level >= 21:
            self.mute(music_space)

        while True:
            try:
                function_level_x = chosen_levels[(count)]
            except IndexError:
                if congratulations == False:
                    if self.level == 26:
                        self.credit_screen()
                    elif self.worlds_unlocked[int((self.level-1)/5)] == False:
                        self.first_unlock = True
                    self.worlds_unlocked[int((self.level-1)/5)] = True
                    self.level_map()

            # Tracks the location of mouse
            mouse_pos = pygame.mouse.get_pos()

            # Color of text on screen
            color_w = (0,0,0)

            # Every world has its own background!
            if self.level >= 0 and self.level < 6:
                self.moving_bg(fieldworld_bg, field_coordinates, field_speed_x, field_speed_y)
            elif self.level >= 6 and self.level < 11:
                self.moving_bg(bg_beachworld, beach_coordinates, beach_speed_x, beach_speed_y)
            elif self.level >= 11 and self.level < 16:
                self.moving_bg(bg_seaworld, sea_coordinates, sea_speed_x, sea_speed_y)
            elif self.level >= 16 and self.level < 21:
                self.moving_bg(bg_snowworld, snow_coordinates, snow_speed_x, snow_speed_y)
            elif self.level >= 21:
                self.moving_bg(bg_spaceworld, space_coordinates, space_speed_x, space_speed_y)
                color_w = (255,255,255)

            levelmap_button = self.screen.blit(levelmap_b, (350, 2))

            while one_question == False:
                position = 290, 250
                if score < 10:
                    if mistakes != []:
                        sommetje = random.choice([function_level_x, function_level_x, self.repeat_mistakes])(already_done, one_question, mistakes)
                    else:
                        sommetje = function_level_x(already_done, one_question, mistakes)
                    one_question = sommetje[0]
                    already_done = sommetje[1]
                    question_int = sommetje[2]
                    print_this = f"{question_int[0]} {question_int[2]} {question_int[1]} = "
                else:
                    if mistakes != []:
                        sommetje = self.repeat_mistakes(already_done, one_question, mistakes)
                        one_question = sommetje[0]
                        question_int = sommetje[2]
                        print_this = f"{question_int[0]} {question_int[2]} {question_int[1]} = "
                    else:
                        score = 0
                        congratulations, one_question = True, True
                        pygame.time.set_timer(congratulationstimerevent, 4000)

            # Determines the action and gives the wanted result
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # Press esc button and go back to menu
                    if event.key == pygame.K_ESCAPE:
                        self.text_surface = self.my_font.render('', True, (0, 0, 0))
                        self.text = ''
                        self.menu()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Click home_button and go back to level map
                    if levelmap_button.collidepoint(mouse_pos):
                        self.text_surface = self.my_font.render('', True, (0, 0, 0))
                        self.text = ''
                        self.level_map()
                self.handle_input(event, color_w)
                if event.type == evaluatetimerevent:
                    pygame.time.set_timer(evaluatetimerevent, 0)
                    evaluate = False
                if event.type == congratulationstimerevent:
                    pygame.time.set_timer(congratulationstimerevent, 0)
                    congratulations, one_question = False, False
                    self.level += 1
                    count += 1

            if congratulations:
                if self.level == 25:
                    self.my_print("Congratulations!", 275, 310, color_w, size=50)
                    self.my_print("You have finished the level mode!", 135, 360, color_w, size=50)
                elif function_level_x == chosen_levels[-1]:
                    self.my_print("Congratulations! You have finished this world!", 175, 220, color_w)
                else:
                    self.my_print("Congratulations! You have finished this level!", 175, 220, color_w)

            # Compare user answer to correct answer
            if len(self.user_input) >= 1:
                check_return = self.check_answer(sommetje[3], question_int, self.user_input, score, mistakes)
                evaluation_string = check_return[0]
                score = check_return[1]
                evaluate = True
                one_question = False
                pygame.time.set_timer(evaluatetimerevent, 1500)

            if evaluate is False and congratulations is False:
                self.print_question(print_this, position, color_w) # Prints exercise

            if evaluate:
                if evaluation_string == "That is correct!":
                    self.my_print(evaluation_string, position[0]-50, position[1]-10, color_w, size=70)
                else:
                    self.my_print(evaluation_string, position[0]-50, position[1]-10, color_w)

            self.my_print(f"score: {min(score, 10)}", 20, 20, color_w, size=70)
            if congratulations == False:
                self.my_print(f"level {self.level}", 600, 20, color_w, size=70)

            pygame.draw.rect(self.screen, (0,255,0), pygame.Rect(20, 75, min(20*(score), 200), 30))
            pygame.draw.rect(self.screen, (128,128,128), pygame.Rect(20, 75, 200, 30), 1)

            if score >= 10 and mistakes != []:
                this_font = pygame.font.Font(None, 30)
                txt = "Well done! We will try your mistakes again to complete this level"
                this_text = this_font.render(txt, True, color_w)
                self.screen.blit(this_text, (20,125))

            # Input_box settings
            if evaluate is False and congratulations is False:
                self.input_box_set(color=color_w)

            # Updates the screen with anything we put in the loop
            pygame.display.update()

            # Capping the fps of the game
            self.clock.tick(120)

    def multiplayer(self, replay, player_1, player_2):
        """This is the function for multiplayer mode."""
        name_1, name_2 = False, False
        start, switch_turn = False, False
        p_1_turn, p_2_turn = False, False
        rounds = 1
        if replay:
            name_1, name_2, start, p_1_turn = True, True, True, True

        turn = 0
        p_1_lives, p_2_lives = 3, 3
        p_1_color = (255,0,0) # Red
        p_2_color = (54,148,255) # Blue

        one_question, evaluate = False, False
        score, p_1_score, p_2_score = 0, 0, 0
        already_done, mistakes = [], []

        evaluatetimerevent = pygame.USEREVENT + 1

        while True:
            if rounds < 2:
                function_level_x = levels[3]
            elif rounds == 2 or rounds == 2.5:
                function_level_x = levels[5]
            elif rounds == 3 or rounds == 3.5:
                function_level_x = levels[6]
            elif rounds == 4 or rounds == 4.5:
                function_level_x = levels[13]
            elif rounds == 5 or rounds == 5.5:
                function_level_x = levels[19]
            elif rounds >=6:
                function_level_x = levels[-1]

            # Tracks the location of mouse
            mouse_pos = pygame.mouse.get_pos()
            self.moving_bg(fieldworld_bg, field_coordinates, field_speed_x, field_speed_y)
            h_button = self.screen.blit(home_button, (350, 2))
            self.mute_button()

            # Determines the action and gives the wanted result
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.text_surface = self.my_font.render('', True, (0, 0, 0))
                        self.text = ''
                        self.menu()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if h_button.collidepoint(mouse_pos):
                        self.text_surface = self.my_font.render('', True, (0, 0, 0))
                        self.text = ''
                        self.input_box = pygame.Rect(460, 248, 190, 50)
                        self.menu()
                    elif self.music_button.collidepoint(mouse_pos):
                        if self.sound:
                            pygame.mixer.music.stop()
                            self.sound = False
                        else:
                            pygame.mixer.music.play(-1)
                            self.sound = True
                if not start:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            start = True
                if name_1 is False or name_2 is False:
                    self.name_choice(event)
                elif name_1 and name_2:
                    self.handle_input(event)
                if event.type == evaluatetimerevent:
                    pygame.time.set_timer(evaluatetimerevent, 0)
                    evaluate = False

            if not start:
                self.my_print("Welcome to multiplayer mode!", 150, 160, size=50)
                self.my_print("Here you can solve fun math questions together with your friends!", 80, 220)
                self.my_print("Press the space bar when you are ready.", 210, 300)

            if name_1 is False and start is True:
                self.my_print("Player 1!", 300, 180, size=60, color=p_1_color)
                self.my_print("Please choose your name: ", 170, 270)
                self.input_box = pygame.Rect(450, 265, 190, 30)
                self.input_box_set(width=100, color=p_1_color)
                if len(self.name) >= 1:
                    player_1 = self.name.lower().title()
                    name_1 = True
                    self.name = ''

            if name_2 is False and name_1 is True:
                self.my_print("Player 2!", 300, 180, size=60, color=p_2_color)
                self.my_print("Please choose your name: ", 170, 270)
                self.input_box = pygame.Rect(450, 265, 190, 30)
                self.input_box_set(width=100, color=p_2_color)
                if len(self.name) >= 1:
                    player_2 = self.name.lower().title()
                    name_2 = True
                    p_1_turn = True
                    self.name = ''

            if name_2:
                while one_question == False:
                    self.input_box = pygame.Rect(460, 248, 190, 50)
                    position = 270, 250
                    sommetje = function_level_x(already_done, one_question, mistakes)
                    one_question = sommetje[0]
                    already_done = sommetje[1]
                    question_int = sommetje[2]
                    print_this = f"{question_int[0]} {question_int[2]} {question_int[1]} = "

                if evaluate is False and start is True and name_1 is True and name_2 is True:
                    if p_1_turn:
                        self.print_question(print_this, position, color=p_1_color) # Prints exercise
                        self.input_box_set(color=p_1_color) # Input box has correct color
                    if p_2_turn:
                        self.print_question(print_this, position, color=p_2_color)
                        self.input_box_set(color=p_2_color)

                if p_1_turn:
                    self.my_print(f"{player_1}, it's your turn!", 240, 150, size=50)
                if p_2_turn:
                    self.my_print(f"{player_2}, it's your turn!", 240, 150, size=50)
                self.my_print(f"{player_1}", 20, 20, size=65, color=p_1_color)
                self.my_print(f"{player_2}", 500, 20, size=65, color=p_2_color)
                self.multiplayer_lives(p_1_heart, p_2_heart, p_1_lives, p_2_lives)

                if len(self.user_input) >= 1:
                    check_return = self.check_answer(sommetje[3], question_int, self.user_input, score, mistakes)
                    evaluation_string = check_return[0]
                    if evaluation_string != "That is correct!":
                        evaluation_string = "You lost a life :("
                    score = check_return[1]
                    if p_1_turn:
                        if score == 0:
                            switch_turn = True
                            p_1_lives -= 1
                        p_1_score += score
                    if p_2_turn:
                        if score == 0:
                            switch_turn = True
                            p_2_lives -= 1
                        p_2_score += score
                    score = 0
                    turn += 1
                    if turn == 5:
                        rounds += 0.5
                        switch_turn = True
                    evaluate = True
                    one_question = False
                    pygame.time.set_timer(evaluatetimerevent, 1500)

                if switch_turn:
                    turn = 0
                    p_1_turn, p_2_turn = p_2_turn, p_1_turn
                    switch_turn = False

                if evaluate:
                    self.my_print(evaluation_string, 240, 280, size=50)

                if rounds == 8:
                    if p_1_lives > p_2_lives:
                        self.multiplayer_end(player_1, player_1, player_2)
                    elif p_2_lives > p_1_lives:
                        self.multiplayer_end(player_2, player_1, player_2)
                    elif p_1_lives == p_2_lives:
                        self.multiplayer_end("tie", player_1, player_2)

                if p_1_lives < 1:
                    self.multiplayer_end(player_2, player_1, player_2)
                elif p_2_lives < 1:
                    self.multiplayer_end(player_1, player_1, player_2)

            pygame.display.update()
            self.clock.tick(120)

    def multiplayer_end(self, winner, p_1, p_2):
        """Function that handles the end of multiplayer.
        It shows a winner and gives two replay options.

        Parameters:
        winner: the name of the winner as a string
        p_1: the name of the first player as a string
        p_2: the name of the second player as a string
        """

        # Prints wanted message depending on the outcome of the game
        while True:
            # Tracks the location of mouse
            mouse_pos = pygame.mouse.get_pos()
            self.moving_bg(fieldworld_bg, field_coordinates, field_speed_x, field_speed_y)
            h_button = self.screen.blit(home_button, (350, 2))
            if winner == p_1:
                self.my_print(f"Congratulations {winner}, you won!", 200, 200, (255,0,0), size=40)
            if winner == p_2:
                self.my_print(f"Congratulations {winner}, you won!", 200, 200, (54,148,255), size=40)
            if winner == "tie":
                self.my_print("It's a tie!", 200, 200, size=40)
            self.my_print("Press the R to play with the same friend", 210, 300)
            self.my_print("Press the space bar to play with another friend", 200, 350)

            # Determines the action and gives the wanted result
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.text = ''
                        self.multiplayer(False, '', '')
                    elif event.key == pygame.K_r:
                        self.text = ''
                        self.multiplayer(True, p_1, p_2)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if h_button.collidepoint(mouse_pos):
                        self.text = ''
                        self.menu()
            pygame.display.update()
            self.clock.tick(120)

    def time_attack(self):
        """This is the function of the timer mode. It uses a timer that counts down
        from 60 seconds and has three difficulty modes.
        """
        total_time = 60
        time_is_up = False

        one_question, evaluate = False, False
        score = 0
        already_done, mistakes = [], []
        evaluatetimerevent = pygame.USEREVENT + 1
        start = False

        while True:
            self.moving_bg(fieldworld_bg, field_coordinates, field_speed_x, field_speed_y)
            # Tracks the location of mouse
            mouse_pos = pygame.mouse.get_pos()
            timer_button = self.screen.blit(small_menu_button_3, (350, 2))
            self.mute_button()

            # Easy mode displays questions from level 4,
            # which are additions and subtractions under 20.
            if self.difficulty == "easy":
                function_level_x = levels[3]

            # Medium mode displays questions from level 14,
            # which are multiplications.
            if self.difficulty == "medium":
                function_level_x = levels[13]

            # Hard mode displays questions from question 25,
            # which is a mix of all types of exercises.
            if self.difficulty == "hard":
                function_level_x = levels[24]
            
            # Determines the action and gives the wanted result
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.text_surface = self.my_font.render('', True, (0, 0, 0))
                        self.text = ''
                        self.time_menu()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if timer_button.collidepoint(mouse_pos):
                        self.text_surface = self.my_font.render('', True, (0, 0, 0))
                        self.text = ''
                        self.time_menu()
                    elif self.music_button.collidepoint(mouse_pos):
                        if self.sound:
                            pygame.mixer.music.stop()
                            self.sound = False
                        else:
                            pygame.mixer.music.play(-1)
                            self.sound = True

                if start is False:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            start = True
                            time_is_up = False
                            score = 0
                            already_done, mistakes = [], []
                            self.text_surface = self.my_font.render('', True, (0, 0, 0))
                            self.text = ''

                self.handle_input(event)
                if event.type == evaluatetimerevent:
                    pygame.time.set_timer(evaluatetimerevent, 0)
                    evaluate = False

            if not start:
                start_seconds = pygame.time.get_ticks()

            if not time_is_up and not start:
                self.my_print("You have 60 seconds to answer as many questions right as possible!", 60, 220)
                self.my_print("Press the space bar to start...", 210, 300, size=40)

            if time_is_up and start is False:
                self.my_print(f"Your time is up! You finished {self.difficulty} mode!", 200, 160, size=30)
                self.my_print(f"final score: {score}", 245, 230, size=70)
                self.my_print("Press the space bar to start again...", 235, 320)
                one_question, evaluate = False, False

            # When start is set to True the timer starts and questions can be answered
            if start:
                time_passed = (pygame.time.get_ticks() - start_seconds) / 1000
                time_left = total_time - int(time_passed)

                if not time_is_up:
                    self.my_print(str(time_left), 600, 20, size=60)
                    self.my_print(f"score: {score}", 20, 20, size=70)
                    pygame.draw.rect(self.screen, (0,0,255), pygame.Rect(510, 70, min(4*(time_left), 240), 30))
                    pygame.draw.rect(self.screen, (128,128,128), pygame.Rect(510, 70, 240, 30), 1)

                    this_font = pygame.font.Font(None, 50)
                    this_text = this_font.render(f"{self.difficulty} mode", True, (0, 0, 0))
                    self.screen.blit(this_text, (20,80))

                if time_left <= 0:
                    time_is_up = True
                    start = False

                # A question is generated
                while one_question is False:
                    position = 270, 250
                    sommetje = function_level_x(already_done, one_question, mistakes)
                    one_question = sommetje[0]
                    already_done = sommetje[1]
                    question_int = sommetje[2]
                    print_this = f"{question_int[0]} {question_int[2]} {question_int[1]} = "

                if evaluate is False and time_is_up is False:
                    self.print_question(print_this, position)
                    self.input_box_set()

                # The user answer is checked
                if len(self.user_input) >= 1:
                    check_return = self.check_answer(sommetje[3], question_int, self.user_input, score, mistakes)
                    evaluation_string = check_return[0]
                    score = check_return[1]
                    evaluate = True
                    one_question = False
                    pygame.time.set_timer(evaluatetimerevent, 300)

                if evaluate and time_is_up is False:
                    if evaluation_string == "That is correct!":
                        # The input box turns green when the answer is correct
                        pygame.draw.rect(self.screen, (50, 205, 0), self.input_box, 2)
                    else:
                        # The input box turns red when the answer is incorrect
                        pygame.draw.rect(self.screen, (255, 0, 0), self.input_box, 2)

            pygame.display.update()
            self.clock.tick(120)

    def time_menu(self):
        """This is the menu of timer mode, where you can choose the difficulty
        by clicking on a button. There are three difficuties: easy, medium and hard.
        """
        while True:
            # Tracks the location of mouse
            mouse_pos = pygame.mouse.get_pos()

            # Moving field background items (bee and clouds)
            self.moving_bg(fieldworld_bg, field_coordinates, field_speed_x, field_speed_y)

            # Buttons
            button_1 = self.screen.blit(easy_button, (124, 225))
            button_2 = self.screen.blit(medium_button, (324,225))
            button_3 = self.screen.blit(hard_button, (524,225))
            h_button = self.screen.blit(home_button, (360, 2))
            self.mute_button()

            self.my_print("Choose a difficulty!", 270, 150, size=40)

            # Determines the action and gives the wanted result
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if h_button.collidepoint(mouse_pos):
                        self.text = ''
                        self.menu()
                    else:
                        # Mousebuttondown on one of the buttons,
                        # with exception of the music button,
                        # will start the game with that difficulty
                        if button_1.collidepoint(mouse_pos):
                            self.difficulty = "easy"
                            self.time_attack()
                        elif button_2.collidepoint(mouse_pos):
                            self.difficulty = "medium"
                            self.time_attack()
                        elif button_3.collidepoint(mouse_pos):
                            self.difficulty = "hard"
                            self.time_attack()
                        elif self.music_button.collidepoint(mouse_pos):
                            if self.sound:
                                pygame.mixer.music.stop()
                                self.sound = False
                            else:
                                pygame.mixer.music.play(-1)
                                self.sound = True

            pygame.display.update()
            self.clock.tick(120)

    def first_screen(self):
        """The first screen you see when you open the game."""
        pygame.mixer.music.stop()
        while True:

            # Moving field background items (bee and clouds)
            self.moving_bg(fieldworld_bg, field_coordinates, field_speed_x, field_speed_y)
            # Determines the action and gives the wanted result
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.menu()

            self.my_print("Welcome to...", 290, 100, size=50)
            self.my_print("Arithmekids!", 230, 150, size=80)
            self.my_print("This game was made by:", 280, 250)
            self.my_print("Amarise, Jack, Nikki, Siem and Yanna!", 220, 275)
            self.my_print("Press enter to start", 270, 340, size=40)

            pygame.display.update()
            self.clock.tick(120)

    def menu(self):
        """The main menu where you can choose a game mode."""
        # Song does not restart when going from level_map to menu
        if self.music_play is False:
            self.mute(music_field)

        while True:
            # Tracks the location of mouse
            mouse_pos = pygame.mouse.get_pos()

            # Moving field background items (bee and clouds)
            self.moving_bg(fieldworld_bg, field_coordinates, field_speed_x, field_speed_y)

            # Buttons
            clear_button = self.screen.blit(clear_image, (20, 500))
            button_1 = self.screen.blit(menu_button_1, (124, 225))
            button_2 = self.screen.blit(menu_button_2, (324,225))
            button_3 = self.screen.blit(menu_button_3, (524,225))
            self.mute_button()

            # Determines the action and gives the wanted result
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.first_screen()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Mousebuttondown on one of the buttons,
                    # except the music and clear buttons,
                    # will start that particular game mode
                    if button_1.collidepoint(mouse_pos): # Opens Multiplayer mode,
                        # and resets input box
                        self.multiplayer(False, '', '')
                    if button_2.collidepoint(mouse_pos): # Opens Level mode
                        self.level = 1
                        self.level_map()
                    if button_3.collidepoint(mouse_pos): # Opens Timer mode
                        self.time_menu()
                    if self.music_button.collidepoint(mouse_pos):
                        if self.sound:
                            pygame.mixer.music.stop()
                            self.sound = False
                        else:
                            music(music_field)
                            self.sound = True
                    if clear_button.collidepoint(mouse_pos):
                        self.clear_screen()

            pygame.display.update()
            self.clock.tick(120)

    def clear_screen(self):
        """Shows a confirmation screen for deleting all progress."""
        yes_image = pygame.image.load('images/yes_button.png')
        no_image = pygame.image.load('images/no_button.png')
        save_file_deleted = False
        message = False
        messagetimerevent = pygame.USEREVENT + 1

        while True:
            # Creates new screen with text
            transparent_screen = pygame.Surface((800,600))
            transparent_screen.set_alpha(150)
            transparent_screen.fill((255,255,255))
            self.screen.blit(transparent_screen, (0,0))

            self.my_print('Are you sure you want to delete your progress?', 140, 250)
            
            # Tracks the location of mouse
            mouse_pos = pygame.mouse.get_pos()
            
            # Blits button images
            yes_image = pygame.transform.scale(yes_image, (80, 45))
            yes_button = self.screen.blit(yes_image, (250, 300))
            no_image = pygame.transform.scale(no_image, (80, 45))
            no_button = self.screen.blit(no_image, (450, 300))

            # Determines the action and gives the wanted result
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == messagetimerevent:
                    pygame.time.set_timer(messagetimerevent, 0)
                    self.menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button.collidepoint(mouse_pos):
                        # Resets progress
                        self.shelf_file = shelve.open('save_file/save_file')
                        self.shelf_file['world_beach'] = False
                        self.shelf_file['world_sea'] = False
                        self.shelf_file['world_snow'] = False
                        self.shelf_file['world_space'] = False
                        self.shelf_file.close()
                        self.worlds_unlocked = [True, False, False, False, False]
                        save_file_deleted = True
                    elif no_button.collidepoint(mouse_pos):
                        self.menu()
            
            # Creates and shows confirmation message screen
            if save_file_deleted:
                message = True
                save_file_deleted = False
                pygame.time.set_timer(messagetimerevent, 2000)

            if message:
                transparent_screen = pygame.Surface((800,600))
                transparent_screen.set_alpha(150)
                transparent_screen.fill((255,255,255))
                self.screen.blit(transparent_screen, (0,0))
                self.my_print("Your progress has been deleted!", 140, 300, color=(255,0,0), size=50)

            pygame.display.update()
            self.clock.tick(120)

    def level_map(self):
        """The level map of the levels mode with all the worlds."""
        self.mute(music_field)
        level_map_bg = pygame.image.load('images/level_map.png')
        messagetimerevent = pygame.USEREVENT + 1
        message = False

        while True:
            # Blits background image of level map to screen
            self.screen.blit(level_map_bg, (0, 0))

            # Shows text
            self.my_print("Choose a world by pressing", 20, 40, color=(255, 255, 255))
            self.my_print("a button without a lock!", 20, 60, color=(255, 255, 255))

            # Tracks the location of mouse
            mouse_pos = pygame.mouse.get_pos()

            # Blits button images on the screen
            h_button = self.screen.blit(home_button, (360, 2))
            field_world = self.screen.blit(field_button, (32, 480))
            self.mute_button()

            # Blits a locked/unlocked version of the world
            if self.worlds_unlocked[1]:
                beach_world = self.screen.blit(beach_button, (190, 350))
                self.shelf_file = shelve.open('save_file/save_file')
                self.shelf_file['world_beach'] = self.worlds_unlocked[1]
                self.shelf_file.close()
            else:
                beach_world = self.screen.blit(beach_lock, (190, 350))


            if self.worlds_unlocked[2]:
                sea_world = self.screen.blit(sea_button, (395, 285))
                self.shelf_file = shelve.open('save_file/save_file')
                self.shelf_file['world_sea'] = self.worlds_unlocked[2]
                self.shelf_file.close()
            else:
                sea_world = self.screen.blit(sea_lock, (395, 285))


            if self.worlds_unlocked[3]:
                snow_world = self.screen.blit(snow_button, (600, 210))
                self.shelf_file = shelve.open('save_file/save_file')
                self.shelf_file['world_snow'] = self.worlds_unlocked[3]
                self.shelf_file.close()
            else:
                snow_world = self.screen.blit(snow_lock, (600, 210))

            if self.worlds_unlocked[4]: # Starts at level 21
                space_world = self.screen.blit(space_button, (610, 15))
                self.shelf_file = shelve.open('save_file/save_file')
                self.shelf_file['world_space'] = self.worlds_unlocked[4]
                self.shelf_file.close()
            else:
                space_world = self.screen.blit(space_lock, (610, 15))
              
            # Determines the action and gives the wanted result
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == messagetimerevent:
                    pygame.time.set_timer(messagetimerevent, 0)
                    message = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if h_button.collidepoint(mouse_pos):
                        self.menu()
                    elif self.music_button.collidepoint(mouse_pos):
                        if self.sound:
                            pygame.mixer.music.stop()
                            self.sound = False
                        else:
                            pygame.mixer.music.play(-1)
                            self.sound = True
                    else:
                        if field_world.collidepoint(mouse_pos):
                            self.level = 1
                            self.run_game()
                        try:
                            if beach_world.collidepoint(mouse_pos) and self.worlds_unlocked[1]:
                                self.level = 6
                                self.run_game()
                            elif sea_world.collidepoint(mouse_pos) and self.worlds_unlocked[2]:
                                self.level = 11
                                self.run_game()
                            elif snow_world.collidepoint(mouse_pos) and self.worlds_unlocked[3]:
                                self.level = 16
                                self.run_game()
                            elif space_world.collidepoint(mouse_pos) and self.worlds_unlocked[4]:
                                self.level = 21
                                self.run_game()
                        except UnboundLocalError:
                            self.level_map()

            # Shows a text when a new world is unlocked
            if self.first_unlock:
                message = True
                self.first_unlock = False
                pygame.time.set_timer(messagetimerevent, 4000)

            if message: # Message when new world is unlocked
                transparent_screen = pygame.Surface((800,600))
                transparent_screen.set_alpha(150)
                transparent_screen.fill((255,255,255))
                self.screen.blit(transparent_screen, (0,0))
                self.my_print("You have unlocked a new world!", 140, 250, color=(0,128,0), size=50)

            pygame.display.update()
            self.clock.tick(120)

    def moving_credit(self, credit, x_coordinates, y_coordinates, speed):
        """This function makes the credits move over the screen."""
        color_w = (255, 255, 255)
        if y_coordinates[0] > -30:
            y_coordinates[0] -= speed
            self.my_print(credit[0], x_coordinates[0], y_coordinates[0], color_w, size=50)

        if y_coordinates[1] > -20:
            y_coordinates[1] -= speed
            self.my_print(credit[1], x_coordinates[1], y_coordinates[1], color_w, size=40)

        if y_coordinates[2] > -20:
            y_coordinates[2] -= speed
            self.my_print(credit[2], x_coordinates[2], y_coordinates[2], color_w, size=40)

        if y_coordinates[3] > -20:
            y_coordinates[3] -= speed
            self.my_print(credit[3], x_coordinates[3], y_coordinates[3], color_w, size=40)

        if y_coordinates[4] > -20:
            y_coordinates[4] -= speed
            self.my_print(credit[4], x_coordinates[4], y_coordinates[4], color_w, size=40)

        if y_coordinates[5] > -20:
            y_coordinates[5] -= speed
            self.my_print(credit[5], x_coordinates[5], y_coordinates[5], color_w, size=40)
        else:
            creds.credit_order[self.credit_number] = False
            self.credit_number = self.next_credit
            self.next_credit += 1

        if y_coordinates[5] < 500:
            if creds.credit_order[self.next_credit] == False:
                creds.credit_order[self.next_credit] = True

    def credit_screen(self):
        """Player has finished the last level and can now enjoy the credit screen."""
        self.mute(music_credits)
        speed = 0.4

        while True:
            self.moving_bg(credits_bg, credits_coordinates, credits_speed_x, credits_speed_y)
            self.mute_button()

            # Tracks the location of mouse
            mouse_pos = pygame.mouse.get_pos()
            # Determines the action and gives the wanted result
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.first_screen()
                    if event.key == pygame.K_SPACE:
                        if speed < 10:
                            speed = speed * 2
                    if event.key == pygame.K_BACKSPACE:
                        if speed >= 0.4:
                            speed = speed / 2
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.music_button.collidepoint(mouse_pos):
                        if self.sound:
                            pygame.mixer.music.stop()
                            self.sound = False
                        else:
                            music(music_credits)
                            self.sound = True

            if creds.credit_order[-1]:
                if creds.trivia_4_coor[-1] < -20:
                    creds.all_coordinates = creds.all_coordinates_copy[:]
                    creds.credit_order = creds.credit_order_copy[:]
                    self.credit_number = 0
                    self.next_credit = 1
                    self.level_map()
            elif creds.credit_order[self.credit_number]:
                self.moving_credit(creds.all_credits[self.credit_number], creds.all_x_coordinates[self.credit_number],
                    creds.all_coordinates[self.credit_number], speed)
            elif creds.credit_order[self.next_credit]:
                self.moving_credit(creds.all_credits[self.next_credit], creds.all_x_coordinates[self.next_credit],
                    creds.all_coordinates[self.next_credit], speed)

            pygame.display.update()
            self.clock.tick(120)

if __name__ == '__main__':
    game = Game()
    game.first_screen()
    game.menu()
