import pygame, sys, random, time

def ball_animation():
    global ball_speed_x, ball_speed_y
    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1 # Reverse ball speed
    # Collision with left and right walls
    if ball.left <= 0 or ball.right >= screen_width:
        time.sleep(1)
        ball_restart()
        
    # Collision with rectangles
    if ball.colliderect(player) or ball.colliderect(opponent):
        pygame.mixer.Sound.play(beep)
        ball_speed_x *= -1
        
        
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height 

def opponent_ai():
    if opponent.top <= ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height 
        
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))



# General setup
pygame.init() # Initializes pygame
pygame.mixer.init() 
clock = pygame.time.Clock() # To set the frames per second below
pygame.mixer.Sound.play(pygame.mixer.Sound('/Users/zacharyyu/Desktop/other/pygame/Pong/background.mp3') )

# Define sounds
beep = pygame.mixer.Sound('/Users/zacharyyu/Desktop/other/pygame/Pong/beep.mp3')

# Setting up the main window
screen_width = 1280 # Defines the screen's width
screen_height = 850 # Defines the screen's height
screen = pygame.display.set_mode((screen_width, screen_height)) # Displays the screen
pygame.display.set_caption("Pong") # Gives the game a title

# Define rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140) 
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# Define colors
bg_color = (20, 20, 40)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

# Define speeds
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice ((1, -1))
player_speed = 0
opponent_speed = 12

while True:
    # Handling input
    for event in pygame.event.get(): # Checks each event in pygame
        if event.type == pygame.QUIT: # If the event is to quit the program
            # These two functions close the game reliably
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    
    
    ball_animation()
    player_animation()
    opponent_ai()
            
    # Draw background
    screen.fill(bg_color) 
    
    # Draw images/rectangles
    pygame.draw.rect(screen, cyan, player) 
    pygame.draw.rect(screen, cyan, opponent)
    pygame.draw.ellipse(screen, magenta, ball) 
    pygame.draw.aaline(screen, cyan, (screen_width / 2, 0), (screen_width / 2, screen_height))

            
    # Updating the window
    pygame.display.flip() # Draws images on the screen
    clock.tick(60) # 60 FPS