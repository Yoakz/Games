import pygame, sys, random, time

def main():

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Snake")

    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    snake = [pygame.Rect(400, 400, 20, 20)] # List of rectangles in the snake
    direction = (20, 0) # Moves to the right

    move_timer = 0
    move_delay = 6  # Snake moves every 6 frames (10 times per second)

    score = 0
    font = pygame.font.Font(None, 36)
    font1 = pygame.font.Font(None, 150)

    def create_food():
        x = random.randint(0, (screen_width - 20) // 20) * 20
        y = random.randint(0, (screen_height - 20) // 20) * 20
        return pygame.Rect(x, y, 20, 20)

    food = create_food()     

   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 20):  # Can't go up if going down
                    direction = (0, -20)
                elif event.key == pygame.K_DOWN and direction != (0, -20):  # Can't go down if going up
                    direction = (0, 20)
                elif event.key == pygame.K_LEFT and direction != (20, 0):  # Can't go left if going right
                    direction = (-20, 0)
                elif event.key == pygame.K_RIGHT and direction != (-20, 0):  # Can't go right if going left
                    direction = (20, 0)
           
        
        move_timer += 1
        if move_timer >= move_delay:
            move_timer = 0  # Reset timer
            new_head = pygame.Rect(snake[0].x + direction[0], snake[0].y + direction[1], 20, 20)
            snake.insert(0, new_head)
            
            # Check for wall collisions
            if (snake[0].x < 0 or snake[0].x >= screen_width or snake[0].y < 0 or snake[0].y >= screen_height):
                time.sleep(2)
                main()
               
                
            # Check for self collision
            if snake[0] in snake[1:]:
                time.sleep(2)
                main()
                
            
            
            # Check if snake ate food
            if snake[0].colliderect(food):
                food = create_food()  # Create new food
                # Don't remove tail (snake grows)
                score += 1
                if score == 5 or score == 10 or score == 15 or score == 20 or score == 25 or score == 30 or score == 35 or score == 40 or score == 45 or score == 50 or score == 55 or score == 60 or score == 65 or score == 70:
                    move_delay -= 0.5
            else:
                snake.pop()  # Remove tail (normal movement)
            
        screen.fill((0, 0, 0))  # Clear screen with black

        # Draw each segment of the snake
        random_color = random.choice([(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 255)])
        for segment in snake:
            pygame.draw.rect(screen, random_color, segment)  # Green snake

        pygame.draw.rect(screen, (255, 0, 0), food)  # Red food
        
        # Draw score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
            
        
        pygame.display.flip()
        clock.tick(60)
        
    
main()