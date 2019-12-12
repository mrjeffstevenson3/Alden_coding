import pygame
testing = True
# ================================================= INSTANCE VARIABLES ================================================*
# this could be a dictionary called colors accessed by colors['WHITE'] and importable into any game module
# colors and fonts dictionary and objects classes could all be put in another file called nav_obj.py and imported here
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHTGRAY = (170, 170, 170)
DARKGRAY = (96, 96, 96)
BLUE = (51, 153, 215)
GREEN = (153, 240, 51)
TRANSPARENT = (0, 0, 0, 0)

# ===================================================== GAME SETUP ====================================================*

# PYGAME SETUP
pygame.init()
screen_width = 1250
screen_height = 800
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Navigate")
clock = pygame.time.Clock()

# hide the mouse cursor
pygame.mouse.set_visible(testing) # 0 false, 1 true

# (could move to nav_obj.py)
background = pygame.image.load("stars_background.png")

# MUSIC
#intro_music = "intromsc.mp3"
#game_music = "gamemsc.mp3"

#pygame.mixer.music.load(game_music)
#pygame.mixer.music.play(-1, 0)

# OBJECTS (could move to nav_obj.py)
asteroid = pygame.image.load("asteroid.png")
key = pygame.image.load("starkey.png")

# movement speed
speed_x = 0
speed_y = 0

# spaceship starting position
current_x = 15
current_y = screen_height/2

# TEXT/FONTS (could move to nav_obj.py)
L_font = pygame.font.SysFont('Calibri', 70, True, False)
font = pygame.font.SysFont('Calibri', 60, True, False)
font2 = pygame.font.SysFont('Calibri', 30, True, False)
font3 = pygame.font.SysFont('Calibri', 15, True, False)
fonts = {'Calibri70Bold': L_font.render, 'Calibri60Bold': font.render, 'Calibri30Bold': font2.render,
         'Calibri15Bold': font3.render}
# ====================================================== CLASSES ======================================================*
# (could move all to nav_obj.py)

class Asteroid:
    if testing:
        speed = 1
    def __init__(self, x, y, direction, left_bound, right_bound, top_bound, bottom_bound, asteroid, speed):
        self.x = x
        self.y = y
        self.direction = direction
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.top_bound = top_bound
        self.bottom_bound = bottom_bound
        self.asteroid = asteroid
        self.speed = speed

    def move(self):
        """
        x_bound = (0, 1250)
        y_bound = (100, 800)
        direction 0 = up or decreasing y
        direction 1 = right or increasing x
        direction 2 = down or increasing y
        direction 3 = left or decreasing x

        motion:
        x increase ==> moves right
        x decrease ==> moves left
        y increase ==> moves down
        y decrease ==> moves up
        """

        if self.y <= self.top_bound:
            self.direction = 2
        elif self.y >= self.bottom_bound:
            self.direction = 0
        elif self.x <= self.left_bound:
            self.direction = 1
        elif self.x >= self.right_bound:
            self.direction = 3

        if self.direction == 0:
            self.y -= self.speed
        elif self.direction == 1:
            self.x += self.speed
        elif self.direction == 2:
            self.y += self.speed
        elif self.direction == 3:
            self.x -= self.speed
        screen.blit(self.asteroid, (self.x, self.y))

class Key:
    def __init__(self, x, y, key):
        self.x = x
        self.y = y
        self.key = key

    def place(self):
        screen.blit(self.key, (self.x, self.y))

# ====================================================== FUNCTIONS ====================================================*
# (could move all to nav_obj.py)

def square(x):
    return x*x

def make_spaceship (screen, x, y):
    # Dimensions:
    # Width: 100px;
    # Height: 60px

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

def text(text, position, font, color):
    if font in fonts:
        screen.blit(fonts[font](text, True, color), position)
    else:
        raise ValueError('Font not in dictionary of fonts')

def collide(obj, threshold):
    if square((current_x) - (obj.x)) + square((current_y) - (obj.y)) <= threshold:
        return True
    else:
        return False

"""
usages are with colors and fonts dictionaries implemented and perhaps imported from nav_obj.py:
text("Are you scared?", [screen_width/3, screen_height/4], 'Calibri70Bold', colors['WHITE'])

# collison test
collided = False
for a in L1_asteroids:
    if collide(a, 5000):   #<===
        collided = True
        current_x = 0
        current_y = screen_height / 2
        L1key_collected = [False]*3
        deaths += 1
        break

"""

# ======================================================== RUN GAME ===================================================*

level = 2
deaths = 0

# LEVEL ONE CONSTRUCTION
L1_asteroids = []
for i in range(1, 6):
    L1_asteroids.append(Asteroid(i*200, screen_height/2, 2, 0, screen_width-75, 100, screen_height-64, asteroid, 15))

# LEVEL TWO CONSTRUCTION
L2_asteroids = []
L2_asteroids.append(Asteroid(screen_width/2, screen_height/2-75, 3, 10, screen_width/2, 100, screen_height-64, asteroid, 30))
L2_asteroids.append(Asteroid(screen_width/2, screen_height/2+75, 3, 10, screen_width/2-100, 100, screen_height-64, asteroid, 30))
# FINISH THE LEVEL HERE

L2_keys = []
L2_keys.append(Key(25, screen_height/2, key))
L2key_collected = [False]



# GAME INTERFACE
done = False
while not done:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.mixer.music.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -5
            elif event.key == pygame.K_RIGHT:
                speed_x = 5
            elif event.key == pygame.K_UP:
                speed_y = -5
            elif event.key == pygame.K_DOWN:
                speed_y = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_y = 0

    # move the stick figure according to the speed
    current_x += speed_x
    current_y += speed_y

    # screen boundaries -> make the ship (essentially) stop when it hits a wall
    if current_x <= 3 or current_x > screen_width - 100:
        speed_x *= -0.01
    if current_y <= 111 or current_y > screen_height - 60:
        speed_y *= -0.01

    if level == 0:
        pygame.mouse.set_visible(True)
        screen.fill(DARKGRAY)
        title = L_font.render("Are you scared?", True, WHITE)
        answerYes = font.render("Yes", True, GREEN)
        answerNo = font.render("No", True, RED)
        name = font3.render("Created by Alden Hinden-Stevenson", True, WHITE)
        screen.blit(title, [screen_width/3, screen_height/4])
        screen.blit(answerYes, [screen_width/3-30, 2*screen_height/3])
        screen.blit(answerNo, [2*screen_width/3-30, 2*screen_height/3])
        screen.blit(name, [50, screen_height-50])

        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        if event.type == pygame.MOUSEBUTTONUP and x > 2*screen_width/3-40 and x < 2*screen_width/3+40 \
            and y > 2*screen_height/3 and y < 2*screen_height/3+50:
            level = 1
        elif event.type == pygame.MOUSEBUTTONUP and x > screen_width/3-40 and x < screen_width/3+60 \
            and y > 2*screen_height/3 and y < 2*screen_height/3+50:
            done = True

    if level > 0:
        # spawn character
        make_spaceship(screen, current_x, current_y)

        # setup level counter and death counter
        pygame.draw.rect(screen, BLACK, [0, 0, screen_width, 100])
        death_counter = L_font.render("Deaths: " + str(deaths), True, RED)
        level_num = L_font.render("Level: " + str(level), True, GREEN)
        screen.blit(death_counter, [900, 25])
        screen.blit(level_num, [100, 25])

        pygame.mouse.set_visible(testing)

    if level == 1:
        # set target
        pygame.draw.rect(screen, GREEN, [screen_width-100, screen_height/2-150, screen_width, screen_height/2])
        instructions1 = font2.render("TRY TO", True, BLACK)
        instructions2 = font2.render("GET TO", True, BLACK)
        instructions3 = font2.render("HERE!!", True, BLACK)
        screen.blit(instructions1, [screen_width-90, screen_height/2-30])
        screen.blit(instructions2, [screen_width-90, screen_height/2])
        screen.blit(instructions3, [screen_width-90, screen_height/2+30])

        # check for completion
        if current_x > screen_width-150 and screen_height/2-150 < current_y < screen_height/2+150:
            level = 2
            current_x = screen_width/2
            current_y = screen_height/2

        # set asteroids and keys
        for a in L1_asteroids:
            a.move()

        # collison test
        collided = False
        for a in L1_asteroids:
            if square((current_x) - (a.x)) + square((current_y) - (a.y)) <= 5000:
                collided = True
                current_x = 0
                current_y = screen_height / 2
                L1key_collected = [False]*3
                deaths += 1
                break

    if level == 2:
        # set asteroids and keys
        for a in L2_asteroids:
            a.move()
        for collected, key in zip(L2key_collected, L2_keys):
            if not collected:
                key.place()

        # collison test
        collided = False
        for a in L2_asteroids:
            if square((current_x) - (a.x)) + square((current_y) - (a.y)) <= 5000:
                collided = True
                current_x = 0
                current_y = screen_height / 2
                L2key_collected = [False] * 3
                deaths += 1
                break

        # key collection test
        for i, k in enumerate(L2_keys):
            if square((current_x) - (k.x)) + square((current_y) - (k.y)) <= 7000:
                L2key_collected[i] = True
                if all(L2key_collected):
                    level = 2
                    # set level 2 spawn position
                    break

    # update the screen
    pygame.display.flip()
    clock.tick(30)
# end of main
pygame.QUIT