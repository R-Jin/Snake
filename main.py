import pygame 
from snake import Snake, SnakePart

screenSize = (w, h) =  (600, 600)
screen = pygame.display.set_mode(screenSize)


def draw_rect(coords, width, color):
    (x, y) = (coords[0], coords[1])
    pygame.draw.rect(screen, color, (x * width, y * width, width, width))


def draw_snake(snake, gridSize):
    snake_size = w / gridSize

    for part in snake.getParts():
        draw_rect(part.getCoords(), snake_size, "#ffffff")



def main():
    pygame.init()

    pygame.display.set_caption("Snake")

    gridSize = 50

    running = True
    
    snake = Snake()
    i = 0
    while running:
        i += 1
        screen.fill((0,0,0))
        draw_snake(snake, gridSize)
        snake.updateSnake()
        snake.grow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Keyboard inputs
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_w and snake.getHeadDir()[1] != 1):
                    snake.changeDir([0, -1])
                elif (event.key == pygame.K_s and snake.getHeadDir()[1] != -1):
                    snake.changeDir([0, 1])
                elif (event.key == pygame.K_a and snake.getHeadDir()[0] != 1):
                    snake.changeDir([-1, 0])
                elif (event.key == pygame.K_d and snake.getHeadDir()[0] != -1):
                    snake.changeDir([1, 0])



        pygame.time.delay(60)
        pygame.display.update()


if __name__=="__main__":
    main()
