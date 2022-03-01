from snake import Snake, Food 
import random
import pygame 

class Game:

    def __init__(self):
        self.screenSize = (self.w, self.h) =  (600, 600)
        self.screen = pygame.display.set_mode(self.screenSize)
        self.gridSize = 50
        self.food = Food(random.randint(0, self.gridSize - 1), random.randint(0, self.gridSize - 1))
        self.snake = Snake()
        self.grow = False
        self.running = True
        self.score = 0
    
    def run(self):
        while self.running:
            self.collision()
            self.screen.fill((0,0,0))
            self.draw_snake(self.snake)
            self.draw_food(self.food)
            self.snake.updateSnake(self.grow)
            self.food_handler()

            for event in pygame.event.get():
                self.getKey(event)        #returns false if quit is pressed, otherwise check for keypresses
                
            pygame.time.delay(60)
            pygame.display.update()

    def draw_rect(self, coords, width, color):
        (x, y) = (coords[0], coords[1])
        pygame.draw.rect(self.screen, color, (x * width, y * width, width, width))


    def draw_snake(self, snake):
        snake_size = self.w / self.gridSize

        for part in snake.getParts():
            self.draw_rect(part.getCoords(), snake_size, "#ffffff")

    def draw_food(self, food):
        food_size = self.w / self.gridSize
        self.draw_rect(food.getCoords(), food_size, "red")

    def get_score(self):
        return self.score

    def update_score(self):
        self.score += 69

    def food_handler(self):
        headCoord = self.snake.getHead().getCoords()
        if headCoord == self.food.getCoords():
            self.update_score()
            print(self.score)
            self.grow = True
            self.food.updateToNewCoord(self.gridSize, self.snake)
        else: 
            self.grow = False

    def collision(self):
        headCoord = self.snake.getHead().getCoords()
        if (headCoord[0] > self.gridSize - 1 or headCoord[0] < 0) or (headCoord[1] > self.gridSize - 1 or headCoord[1] < 0):
            print("Final score:", self.score)
            self.running = False
        for part in self.snake.getParts()[1:]:
            if part.getCoords() == headCoord:
                print("Final score:", self.score)
                self.running = False
    

    def getKey(self, event):
        if event.type == pygame.QUIT:
            print("Final score:", self.score)
            self.running = False
            
        # Keyboard inputs
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_w and self.snake.getDir()[1] != 1):
                self.snake.changeDir((0, -1))
            elif (event.key == pygame.K_s and self.snake.getDir()[1] != -1):
                self.snake.changeDir((0, 1))
            elif (event.key == pygame.K_a and self.snake.getDir()[0] != 1):
                self.snake.changeDir((-1, 0))
            elif (event.key == pygame.K_d and self.snake.getDir()[0] != -1):
                self.snake.changeDir((1, 0))