import pygame
import math

intro_text = 'Welcome to Animal Rush !'  # Message for introduction screen.
final1 = 'Both Player 1 and Player 2 won !'  # Final text if both player draw.
final2 = 'Player 1 won !'  # Final text if player 1 wins.
final3 = 'Player 2 won !'  # Final text if player 2 wins.

bg_music = 'bgmusic.mp3'  # Background music for the game.

font_type = 'comicsans'  # Font-type for all the texts.

c1 = 255  # RGB values for background colour of intro and end text screens.
c2 = 0
c3 = 0

current_time = 2
last_time = 2

w1 = 255  # RGB values for text colour.
w2 = 255
w3 = 255

win = pygame.display.set_mode((1000, 870))  # Setting size of game screen.

pygame.display.set_caption('Animal Rush')  # Setting caption name.

icon_image = 'p2.png'  # Set icon image.
background_image = 'bg.png'  # Set the background image for the game here.
player1_image = 'p1.png'  # Set player 1 image.
player2_image = 'p2.png'  # Set player 2 image.

enemy = []  # Initializing list to store enemy images.

for i in range(0, 8):  # Loading enemy images.
    enemy.append(pygame.image.load('tree.png').convert_alpha())

enemy.append(pygame.image.load('boat.png').convert_alpha())
enemy.append(pygame.image.load('boat.png').convert_alpha())
enemy.append(pygame.image.load('boat2.png').convert_alpha())
enemy.append(pygame.image.load('boat2.png').convert_alpha())
enemy.append(pygame.image.load('boat.png').convert_alpha())
enemy.append(pygame.image.load('boat.png').convert_alpha())
enemy.append(pygame.image.load('boat2.png').convert_alpha())
enemy.append(pygame.image.load('boat2.png').convert_alpha())
enemy.append(pygame.image.load('boat.png').convert_alpha())
enemy.append(pygame.image.load('boat.png').convert_alpha())

vel = 6  # Setting speed for both player.
evel = 8  # Setting speed for boats (for level 1).

enemyx = [  # Storing x co-ordinates of enemies in a list.
    70,
    320,
    570,
    820,
    620,
    870,
    120,
    370,
    0,
    500,
    250,
    750,
    330,
    830,
    0,
    500,
    660,
    160,
    ]

enemyy = [  # Storing y co-ordinates of enemies in a list.
    160,
    320,
    480,
    640,
    160,
    320,
    480,
    640,
    80,
    80,
    240,
    240,
    400,
    400,
    560,
    560,
    720,
    720,
    ]
