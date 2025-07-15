import pygame, sys, random, time

pygame.init()
clock = pygame.time.Clock()

screen_width = 1050
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

player = pygame.Rect(425, 700, 150, 30)
player_speed = 0

ball = pygame.Rect(425, 400, 35, 35)
ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = 4 


bricks = [pygame.Rect(50, 300, 150, 50), pygame.Rect(250, 300, 150, 50), pygame.Rect(450, 300, 150, 50), pygame.Rect(650, 300, 150, 50), pygame.Rect(850, 300, 150, 50), pygame.Rect(50, 200, 150, 50), pygame.Rect(250, 200, 150, 50), pygame.Rect(450, 200, 150, 50), pygame.Rect(650, 200, 150, 50), pygame.Rect(850, 200, 150, 50), pygame.Rect(50, 100, 150, 50), pygame.Rect(250, 100, 150, 50), pygame.Rect(450, 100, 150, 50), pygame.Rect(650, 100, 150, 50), pygame.Rect(850, 100, 150, 50)]

font = pygame.font.Font(None, 200)
score_font = pygame.font.Font(None, 36)
score = 15

def player_animation():
    player.x += player_speed
    if player.x <= 0:
        player.x = 0
    elif player.x >= screen_width - 150:
        player.x = screen_width - 150
        
def ball_animation():
    global ball_speed_x, ball_speed_y, bricks, score
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.x >= screen_width or ball.x <= 0:
        ball_speed_x *= -1
    if ball.y <= 0:
        ball_speed_y *= -1
    
    
    if ball.colliderect(player):
        ball_speed_y *= -1
    
    # CLAUDE
    for i in range(len(bricks)):
        if ball.colliderect(bricks[i]):
            ball_speed_y *= -1
            bricks.pop(i)
            score -= 1
            break
    # CLAUDE

    
    
won = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed -= 10
            elif event.key == pygame.K_RIGHT:
                player_speed += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_speed += 10
            elif event.key == pygame.K_RIGHT:
                player_speed -= 10


    screen.fill(black)
                
    player_animation()
    ball_animation()
    if not bricks:
        won = True
        win = font.render("YOU WIN!", True, green)
        screen.blit(win, (200, 300))
        
    if ball.y >= screen_height:
        won = True
        lose = font.render("GAME OVER!", True, red)
        screen.blit(lose, (100, 300))
    

    if won == False:
        pygame.draw.rect(screen, white, player)
        pygame.draw.ellipse(screen, green, ball)
        
        score_text = score_font.render(f"Bricks remaining: {score}", True, white)
        screen.blit(score_text, (20, 20))
        
        for brick in bricks[0:5]:
            pygame.draw.rect(screen, blue, brick)
        
        for brick in bricks[5:10]:
            pygame.draw.rect(screen, red, brick)
        
        for brick in bricks[10:15]:
            pygame.draw.rect(screen, blue, brick)

   
    pygame.display.flip()
    clock.tick(60)