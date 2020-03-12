import pygame
import math
from config import *  # Import all data from config.py file

pygame.init()

font = pygame.font.SysFont(font_type, 30, True)
# declaring font variable which will be used for all texts in the game.

pygame.mixer.music.load(bg_music)
# Setting background music for the game.

pygame.mixer.music.play(-1)

icon = pygame.image.load(icon_image)  # Setting icon for the game.
pygame.display.set_icon(icon)

player1 = pygame.image.load(player1_image).convert_alpha()
# Loading image for player 1.

player2 = pygame.image.load(player2_image).convert_alpha()
# Loading image for player 2.

x1 = 470  # Seting co-ordinates for the players when they respawn.
y1 = 805
x2 = 470
y2 = 4
win1 = 0  # Initialising number of wins as 0 for both players.
win2 = 0
flag = 0
count = 1  # Variable to keep track of number of rounds that have happened.
score1 = 10000  # Initializing score as 10000 for both players.
score2 = 10000

current_player = 1  # Player 1 will start the game.

def compute_distance(x1, x2, y1, y2):
    dist = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return dist


start = True

while start:

    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False  # Move to game if user clicks close button.

    win.fill((c1, c2, c3))  # Setting background colour.
    text2 = font.render(intro_text, 1, (w1, w2, w3))
    win.blit(text2, (340, 425))  # Wrting introduction text on the screen.

    pygame.display.update()
    pygame.time.delay(2000)
    start = False

background = pygame.image.load('bg.png').convert_alpha()
# Setting background image for the game.

run = True

while run and count <= 6:

    pygame.time.delay(20)

    # #################  PLAYER 1 #################

    if current_player is 1:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                # Move to final text screen if user clicks close button

            if event.type == pygame.KEYUP:
                flag = 0  # Resseting flag if key release is detected

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP] and y1 > 5 and flag is 0:
                # Checking which key to awarding points accardingly.
                flag = 1
                # If key up or down is pressed then set flag.
                y1 -= 80
                score1 = score1 + 10000
            if keys[pygame.K_DOWN] and y1 < 800 and flag is 0:
                flag = 1
                y1 += 80
                score1 = score1 - 10000

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x1 >= 3:  # Checking key and moving.
            x1 -= vel

        if keys[pygame.K_RIGHT] and x1 <= 1000 - 60 - vel:
            x1 += vel

        current_time = pygame.time.get_ticks() // 1000 - last_time
        score1 = score1 - current_time

        enemyx[8] = enemyx[8] + evel + 4 * win1  # Setting obstacles positions.
        enemyx[9] = enemyx[9] + evel + 4 * win1
        enemyx[10] = enemyx[10] - evel - 4 * win1
        enemyx[11] = enemyx[11] - evel - 4 * win1
        enemyx[12] = enemyx[12] + evel + 4 * win1
        enemyx[13] = enemyx[13] + evel + 4 * win1
        enemyx[14] = enemyx[14] - evel - 4 * win1
        enemyx[15] = enemyx[15] - evel - 4 * win1
        enemyx[16] = enemyx[16] + evel + 4 * win1
        enemyx[17] = enemyx[17] + evel + 4 * win1

        for i in range(8, 18):  # Putting obastacles in screen.
            if enemyx[i] > 1000:
                enemyx[i] = -70
            elif enemyx[i] < -70:
                enemyx[i] = 1000

        win.blit(background, (0, 0))  # Display background image.

        for i in range(0, 18):  # Checking if collision has occured.
            dist = compute_distance(enemyx[i], x1, enemyy[i], y1)
            if dist < 50 and run is True:
                count = count + 1  # Set variables is collision occured.
                current_player = 2
                x2 = 470
                y2 = 4

        if y1 <= 10 and x1 >= 460 and x1 <= 480:
            # Checking if the player has reached his final destination.
            win1 = win1 + 1  # Set variables if player reached.
            count = count + 1
            current_player = 2
            x2 = 470
            y2 = 4

        for i in range(0, 18):
            win.blit(enemy[i], (enemyx[i], enemyy[i]))
            # Printing all the enemies on the screen.

        win.blit(player1, (x1, y1))  # Printing the player on the screen.

        dis1 = score1 // 1000
        dis2 = score2 // 1000

        text1 = font.render('Player 1 : ' + str(dis1), 1, (w1, w2, w3))
        win.blit(text1, (10, 825))  # Printing score for player 1 on screen.

        text2 = font.render('Player 2 : ' + str(dis2), 1, (w1, w2, w3))
        win.blit(text2, (10, 25))  # Printing score for player 2 on the screen.

        pygame.display.update()  # Updating the screen

        if current_player is 2:  # Checking if it is player 2's turn now.
            pygame.time.delay(2000)
            last_time = current_time

            if count > 2:
                score2 = score2 + 10000  # Setting player 2's score.
    elif current_player is 2:

        # #################  PLAYER 2 #################

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                # Move to final text screen if user clicks close button

            if event.type == pygame.KEYUP:
                flag = 0  # Resseting flag if key release is detected

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w] and y2 > 5 and flag is 0:
                # Checking key pressed and moving, awarding points accardingly.
                flag = 1  # If key up or down is pressed then set flag.
                y2 -= 80
                score2 = score2 - 10000
            if keys[pygame.K_s] and y2 < 800 and flag is 0:
                flag = 1
                y2 += 80
                score2 = score2 + 10000

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and x2 >= 3:  # Checking key pressed and moving.
            x2 -= vel

        if keys[pygame.K_d] and x2 <= 1000 - 60 - vel:
            x2 += vel

        current_time = pygame.time.get_ticks() // 1000 - last_time
        score2 = score2 - current_time

        enemyx[8] = enemyx[8] + evel + 4 * win2  # Setting obstacles positions.
        enemyx[9] = enemyx[9] + evel + 4 * win2
        enemyx[10] = enemyx[10] - evel - 4 * win2
        enemyx[11] = enemyx[11] - evel - 4 * win2
        enemyx[12] = enemyx[12] + evel + 4 * win2
        enemyx[13] = enemyx[13] + evel + 4 * win2
        enemyx[14] = enemyx[14] - evel - 4 * win2
        enemyx[15] = enemyx[15] - evel - 4 * win2
        enemyx[16] = enemyx[16] + evel + 4 * win2
        enemyx[17] = enemyx[17] + evel + 4 * win2

        for i in range(8, 18):  # Bringing obastacles back in screen.
            if enemyx[i] > 1000:
                enemyx[i] = -70
            elif enemyx[i] < -70:
                enemyx[i] = 1000

        win.blit(background, (0, 0))  # Display background image.

        for i in range(0, 18):  # Checking if collision has occured.
            dist = compute_distance(enemyx[i], x2, enemyy[i], y2)
            if dist < 50 and run is True:  # Set variables if hits obstacle.
                count = count + 1
                current_player = 1
                x1 = 470
                y1 = 805

        if y2 >= 800 and x2 >= 460 and x2 <= 480:
            # Checking if the player has reached his final destination.
            win2 = win2 + 1  # Updating variables if player 2 has completed.
            count = count + 1
            current_player = 1
            x1 = 470
            y1 = 805

        for i in range(0, 18):  # Printing all the enemies on the screen.
            win.blit(enemy[i], (enemyx[i], enemyy[i]))

        win.blit(player2, (x2, y2))  # Printing the player on the screen.

        dis1 = score1 // 1000
        dis2 = score2 // 1000

        text1 = font.render('Player 1 : ' + str(dis1), 1, (w1, w2, w3))
        win.blit(text1, (10, 825))  # Printing score for player 1.

        text2 = font.render('Player 2 : ' + str(dis2), 1, (w1, w2, w3))
        win.blit(text2, (10, 25))  # Printing score for player 2.

        pygame.display.update()  # Updating the screen.

        if current_player is 1:  # Checking if it is player 1's turn next
            pygame.time.delay(2000)
            last_time = current_time

            if count < 6:
                score1 = score1 + 10000  # Setting score for player 1.

end = True

while end:  # Final message screen.

    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = False  # Close the game if user hits close button

    win.fill((c1, c2, c3))  # Printing the background

    if score1 == score2:
        # Checking condition and declaring the winner(s) accordingly.
        text2 = font.render(final1, 1, (w1, w2, w3))
        win.blit(text2, (340, 425))

    if score1 > score2:
        text2 = font.render(final2, 1, (w1, w2, w3))
        win.blit(text2, (430, 425))

    if score1 < score2:
        text2 = font.render(final3, 1, (w1, w2, w3))
        win.blit(text2, (430, 425))

    pygame.display.update()  # Updating the screen.

pygame.quit()
