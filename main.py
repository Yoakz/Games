import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Rain Dodge")

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.Rect(500, 700, 20, 40)
player_speed = 0

random_x = random.randrange(50, 950)
raindrop = [pygame.Rect(random_x, 100, 200, 300),pygame.Rect(random.randrange(50, 950), 100, 200, 300)]

white = (255, 255, 255)
blue = (0, 155, 255)
red = (255, 0, 0)

score = 0
font = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 200)
game_over = False

def player_animation():
    global game_over
    player.x += player_speed
    if player.x <= 0:
        player.x = 0
    elif player.x >= screen_width - 20:
        player.x = screen_width - 20
        
    if player.colliderect(raindrop[0]):
        game_over = True
    elif player.colliderect(raindrop[1]):
        game_over = True
    
    
    
    
def raindrop_animation():
    global score
    
    raindrop[0].y += 4
    raindrop[1].y += 4
    if raindrop[0].y >= screen_height:
        score += 1
        raindrop.pop()
        raindrop.insert(0, pygame.Rect(random.randrange(50, 950), 100, 200, 300))
        raindrop.insert(1, pygame.Rect(random.randrange(50, 950), 100, 200, 300))
        pygame.draw.rect(screen, blue, raindrop[0])
        pygame.draw.rect(screen, blue, raindrop[1])



    
while True:
    if game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_speed -= 4
                elif event.key == pygame.K_RIGHT:
                    player_speed += 4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player_speed += 4
                elif event.key == pygame.K_RIGHT:
                    player_speed -= 4          
        player_animation()
        raindrop_animation()
                
                
        screen.fill((0, 0, 0))
                
        score_text = font.render(f"Score: {score}", True, white)
        screen.blit(score_text, (20, 20))
                
        pygame.draw.rect(screen, white, player)
        pygame.draw.rect(screen, blue, raindrop[0])
        pygame.draw.rect(screen, blue, raindrop[1])
                    
        pygame.display.flip()
        clock.tick(60)

    elif game_over == True:
        screen.fill((0, 0, 0))
        game_over_text = font1.render("GAME OVER", True, red)
        screen.blit(game_over_text, (75, 300))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            



