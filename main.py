import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()

screen_width = 900
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fish Tank Simulator")

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
bg_color = (173, 216, 230)

# Lists to store different fish variables
fish_x = [100, 200, 300, 400, 500, 600]
fish_y = [150, 250, 350, 450, 550, 650]
fish_speed = [2, -1, 3, 1, -4, -2]
fish_hunger = [0, 10, 2, 5, 0, 1]

# Empty lists to store position of food
food_x = []
food_y = []

# Other variables
food_on_screen = False
font = pygame.font.Font(None, 36)
stopwatch = 0

def display_stopwatch():
    display = font.render(f"Time: {round(stopwatch, 1)}", True, white)
    screen.blit(display, (150, 30))

def animate_fish():
    for i in range(len(fish_x)):
        fish_x[i] += fish_speed[i]
        # If fish collides with screen borders, reverse direction of that fish
        if fish_x[i] <= 0 or fish_x[i] >= screen_width - 25 or fish_y[i] <= 0 or fish_y[i] >= screen_height - 100:
            fish_speed[i] *= -1

        pygame.draw.ellipse(screen, white, pygame.Rect(fish_x[i], fish_y[i], 90, 50))

def draw_food():
    global food_on_screen
    
    for _ in range(len(food_x)):
        food_on_screen = True
        pygame.draw.ellipse(screen, white, pygame.Rect(food_x[0], food_y[0], 75, 75))
        


def food_fish():
    for i in range(len(fish_x)):
        global food_on_screen, fish_hunger
        
        # Move all fish towards food depending on where the food is
        if food_x and food_y:
            if food_x[0] > fish_x[i]:
                fish_x[i] += 1
            if food_x[0] < fish_x[i]:
                fish_x[i] -= 1
            if food_y[0] > fish_y[i]:
                fish_y[i] += 1
            if food_y[0] < fish_y[i]:
                fish_y[i] -= 1
            
            # Collision square around food to see if fish enters it
            # Reset hunger of that fish
            if food_x[0] - 60 <= fish_x[i] and food_x[0] + 60 >= fish_x[i] and food_y[0] - 60 <= fish_y[i] and food_y[0] + 60 >= fish_y[i]:
                food_on_screen = False
                food_x.pop(0)
                food_y.pop(0)
                
                fish_hunger[i] = 0

def hunger_management():
    global fish_hunger, fish_x, fish_y, fish_speed
    
    # Backwards loop to remove fish if hunger gets too high
    for i in range(len(fish_hunger) - 1, -1, -1):
        fish_hunger[i] += 0.05
        print(fish_hunger)
        if 0 < fish_hunger[i] <= 30:
            pygame.draw.ellipse(screen, green, pygame.Rect(fish_x[i], fish_y[i], 90, 50))
            
        elif 30 < fish_hunger[i] <= 70:
            pygame.draw.ellipse(screen, yellow, pygame.Rect(fish_x[i], fish_y[i], 90, 50))
            
        elif 70 < fish_hunger[i] < 100:
            pygame.draw.ellipse(screen, red, pygame.Rect(fish_x[i], fish_y[i], 90, 50))
        
        if fish_hunger[i] >= 100:
            fish_x.pop(i)
            fish_y.pop(i)
            fish_speed.pop(i)
            fish_hunger.pop(i)

def fish_count():
    global fish_x
    
    num_of_fish = len(fish_x)
    fish_text = font.render(f"Fish: {num_of_fish}", True, white)
    screen.blit(fish_text, (30, 30))

def add_new_fish():
    global fish_x, fish_y, fish_speed, fish_hunger
    
    rand_x = random.randrange(200, 700)
    rand_y = random.randrange(200, 700)
    rand_speed = random.randrange(-5, 5)
    fish_x.append(rand_x)
    fish_y.append(rand_y)
    fish_speed.append(rand_speed)
    fish_hunger.append(0)
    
def get_random_x():
    return random.randrange(70, 150)

def get_random_y():
    return random.randrange(40, 100)

lose = False

while True:
    if not fish_x:
        lose = True
    
    if lose == False:
        stopwatch += 0.015
        if stopwatch >= 180:
            screen.fill(black)
            font = pygame.font.Font(None, 100)
            text = font.render("KEPT FISH HEALTHY", True, white)
            screen.blit(text, (100, 300))
            
            text2 = font.render("GOOD JOB!", True, green)
            screen.blit(text2, (250, 450))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
        else:
            bg = pygame.image.load("Fish Tank Simulator/background.jpg")
            scaled_bg = pygame.transform.scale(bg, (1000, 1000))
            screen.blit(scaled_bg, (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Add the mouse coordinates as food coordinates when you click left mouse button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if food_on_screen == False:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        food_x.append(mouse_x)
                        food_y.append(mouse_y) 
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if len(fish_x) < 15: 
                            add_new_fish()

            animate_fish()
            hunger_management()
            draw_food()
            food_fish() 
            fish_count() 
            display_stopwatch()
                  
    elif lose == True:
        screen.fill(black)
        font = pygame.font.Font(None, 100)
        lose_text = font.render("NO MORE FISH LEFT!", True, red)
        screen.blit(lose_text, (100, 200))
        
        data_text = font.render(f"TIME SURVIVED: {round(stopwatch)}s", True, white)
        screen.blit(data_text, (100, 350))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
    pygame.display.flip()
    clock.tick(60)