import keyboard
import pygame
import time

# Initialize Pygame
pygame.mixer.init()

# Define the sound mappings
sound_mapping = {
    'a': 'yamate.mp3',
    'b': 'ahh.mp3',
    'c': 'oheyy.mp3',
    # 'd': 'dattebayo.mp3',
    # 'e': 'indian-music-bass-boosted.mp3',
    # 'c': 'narutoooo.mp3',
    'f': 'suiiiiiiiiiii.mp3',
    'g': 'UWU Sound.mp3',
    # 'h': 'sachin.mp3',
    # 'i': 'Voicy_ You son of a bitch.mp3',
    'j': 'Voicy_angry anime girl rage.mp3',
    'k': 'Voicy_Anime girl says something cute.mp3',
    'l': 'Voicy_Anime moan meme.mp3',
    'm': 'Voicy_Anime Sound.mp3',
    'n': 'Voicy_Gear Fourth - Monkey D. Luffy.mp3',
    'o': 'Voicy_Hentai Animesample10.mp3',
    'p': 'never_gonna_pass.mp3',
    'q': 'Voicy_Meduko Healed.mp3',
    'r': 'Voicy_Mirai Zura!.mp3',
    # 's': 'Voicy_Nami asks Luffy for help.mp3',
    't': 'Voicy_Of Course I Will! (Luffy).mp3',
    'u': 'Voicy_oh my god anime female.mp3',
    # 'v': 'Voicy_Quit your yappin.mp3',
    # 'w': 'Voicy_Shut up!.mp3',
    'x': 'Voicy_That Isnt Fair.mp3',
    'y': 'Voicy_The City of Gold is in the Sky! (Luffy).mp3',
    'z': 'yt1s_wU4BGgD.mp3'
   
}

# Load sounds into Pygame
sounds = {}
for key, sound_file in sound_mapping.items():
    sounds[key] = pygame.mixer.Sound(sound_file)

# Keyboard event callback
def on_key_press(event):
    key = event.name
    if key in sounds:
        sound = sounds[key]
        sound.play()
        # time.sleep(2)
        # sound.stop()

# Register the callback function for key presses
keyboard.on_press(on_key_press)

# Keep the program running
keyboard.wait()
