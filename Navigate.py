import pygame

# ================================================= INSTANCE VARIABLES ================================================*

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHTGRAY = (170, 170, 170)
DARKGRAY = (96, 96, 96)
BLUE = (51, 153, 215)
GREEN = (153, 240, 51)

# ====================================================== FUNCTIONS ====================================================*

# ideally, this funciton would not actually be a part of the main game page, but rather it would be a part of the Spaceship class
# i need to create classes for objects such as Spaceship and Obstacle

# i could control the movement of the obstacles pretty much the same way as i did with the spaceship, except i would preset them
# ...instead of responding to user input

# the only major concern i have is accounting for collisions and when the spaceship hits an obstacle that's moving

def make_spaceship (screen, x, y):
    # Ship Body
    pygame.draw.ellipse(screen, DARKGRAY, (x+5, y, 90, 60))
    pygame.draw.ellipse(screen, LIGHTGRAY, (x, y, 100, 50))

    # Red Dots
    pygame.draw.ellipse(screen, RED, (x+45, y+36, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+23, y+32, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+67, y+32, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+7, y+20, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+83, y+20, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+18, y+6, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+72, y+6, 10, 10))

    # Ship Cabin
    pygame.draw.ellipse(screen, BLUE, (x+20, y-10, 60, 45))

    # Alien
    pygame.draw.line(screen, GREEN, (x+45, y+32), (x+48, y+10), 5)
    pygame.draw.line(screen, GREEN, (x+55, y+32), (x+58, y+10), 5)
    pygame.draw.ellipse(screen, WHITE, (x+43, y, 10, 15))
    pygame.draw.ellipse(screen, WHITE, (x+53, y, 10, 15))
    pygame.draw.ellipse(screen, BLACK, (x+46, y+3, 5, 8))
    pygame.draw.ellipse(screen, BLACK, (x+56, y+3, 5, 8))

    # Dimensions
    # Width: 100px; Height: 60px


# ===================================================== GAME SETUP ====================================================*

pygame.init()
screen_width = 1250
screen_height = 800
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Navigate")
background = pygame.image.load("stars_background.png")

clock = pygame.time.Clock()

# hide the mouse cursor
pygame.mouse.set_visible(0) # 0 false, 1 true

# movement speed
speed_x = 0
speed_y = 0

# spaceship starting position
current_x = 0
current_y = screen_height/2

'''
# MUSIC
intro_music = "intromsc.mp3"
game_music = "gamemsc.mp3"

pygame.mixer.music.load(game_music)
pygame.mixer.music.play(-1, 0)
'''

# ======================================================== GAME =======================================================*

# the game is run through a loop, which checks itself first for user input events
# first check to see if the game has been quit, if it is, then the game loop boolean will become false, and the game will end upon the next iteration
# the elifs are the keyboard inputs from the user
# im using the arrow keys to change the "speed" of the character by increasing or decreasing the x, y coordinates of the character...
# ...when the arrow keys are pressed


done = False
while not done:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.mixer.music.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -3
            elif event.key == pygame.K_RIGHT:
                speed_x = 3
            elif event.key == pygame.K_UP:
                speed_y = -3
            elif event.key == pygame.K_DOWN:
                speed_y = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_y = 0



    # move the stick figure according to the speed
    current_x += speed_x
    current_y += speed_y

    # screen boundaries -> make the ship (essentially) stop when it hits a wall
    if current_x <= 0 or current_x > screen_width-100:
        speed_x *= -0.01
    if current_y <= 11 or current_y > screen_height-60:
        speed_y *= -0.01
    # starts_background replaces white
    # screen.fill(WHITE)

    make_spaceship(screen, current_x, current_y)

    # update the screen
    pygame.display.flip()
    clock.tick(60)
# end of main
pygame.QUIT