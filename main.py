import pygame 
from main import Snake

size = (w, h) =  (600, 600)
screen = pygame.display.set_mode(size)


def gen_grid(size):
    """ Generating the grid for the board """

    grid = []
    for row in range(size):
        grid.append([])
        for col in range(size):
            grid[row].append(0)

    return grid


def draw_grid(grid):
    """ Draw the cells depending on what state they are in. White for living and black for dead """

    square_w = w / len(grid)
    h_space = 0
    for row in range(len(grid)):
        w_space = 0
        for col in range(len(grid)):
            if grid[row][col]:
                pygame.draw.rect(screen, "#ffffff", (0 + w_space, 0 + h_space, square_w, square_w))
            else:
                pygame.draw.rect(screen, "#000000", (0 + w_space, 0 + h_space, square_w, square_w))
            w_space += square_w
        h_space += square_w


def main():
    pygame.init()

    pygame.display.set_caption("Snake")


    gridSize = 50

    grid = gen_grid(gridSize)

    running = True
    
    while running:

        draw_grid(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        pygame.display.update()


if __name__=="__main__":
    main()
