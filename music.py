"This file holds the music settings."
import pygame

def music(music_world):
    """This function makes it possible to play
        different songs as background music.
        It also makes sure that the song repeats itself.

        Parameter:
        music_world: the song that should be played

        Returns: song playing on repeat
    """
    pygame.mixer.music.load(music_world)
    play_music = pygame.mixer.music.play(-1)
    return play_music

# Loads the image made for the sound button
sound_button = pygame.image.load('buttons/unmuted_button.png')

# Changes the size of the sound button
sound_button = pygame.transform.scale(sound_button, (60, 60))

no_sound_button = pygame.image.load('buttons/muted_button.png')
no_sound_button = pygame.transform.scale(no_sound_button, (60, 60))

# These variables decide which song will be played in which world
music_field = 'music/bensound-cute.mp3'
music_field_world = 'music/bensound-smile.mp3'
music_beach = 'music/bensound-ukulele.mp3'
music_sea = 'music/bensound-psychedelic.mp3'
music_snow = 'music/bensound-littleidea.mp3'
music_space = 'music/bensound-enigmatic.mp3'
music_credits = 'music/bensound-adventure.mp3'
