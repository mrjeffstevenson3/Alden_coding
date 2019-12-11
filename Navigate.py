import pygame

# ================================================= INSTANCE VARIABLES ================================================*

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHTGRAY = (170, 170, 170)
DARKGRAY = (96, 96, 96)
BLUE = (51, 153, 215)
GREEN = (153, 240, 51)

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
pygame.mouse.set_visible(0) # 0 false, 1 true


background = pygame.image.load("stars.jpg")

# MUSIC
#intro_music = "intromsc.mp3"
#game_music = "gamemsc.mp3"

#pygame.mixer.music.load(game_music)
#pygame.mixer.music.play(-1, 0)

# OBJECTS
asteroid = pygame.image.load("asteroid.png")


# movement speed
speed_x = 0
speed_y = 0

# spaceship starting position
current_x = 0
current_y = screen_height/2

# ====================================================== CLASSES ======================================================*

class Asteroid:
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
        y_bound = (0, 800)
        direction 0 = left or decreasing x
        direction 1 = right or increasing x
        direction 2 = up or decreasing y
        direction 3 = down or increasing y

        motion:
        x increase ==> moves right or d
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


# ====================================================== FUNCTIONS ====================================================*

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



# ======================================================== RUN GAME ===================================================*

asteroids = []

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

    for i in range(1, 6):
        asteroids.append(Asteroid(i*100, screen_height/2, 2, 0, screen_width, 0, screen_height, asteroid, 10))
    for a in asteroids:
        a.move()

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

    # OBJECT CREATION
    make_spaceship(screen, current_x, current_y)

    # update the screen
    pygame.display.flip()
    clock.tick(24)
# end of main
pygame.QUIT