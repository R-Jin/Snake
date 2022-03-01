import pygame 
from game import Game

pygame.init()
 

def main():
    game = Game()
    pygame.init()
    pygame.display.set_caption("Snake")

    X = game.w
    Y = game.h
    font = pygame.font.Font("Roboto-Black.ttf", 32)
    text1 = font.render('Press space to start', True, (128, 0, 0))
    textRect = text1.get_rect()
    textRect.center = (X // 2, Y // 2)

    while True:
        game.screen.fill("black")
        game.screen.blit(text1, textRect)
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                break

            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    game.run()

        if not game.running:
            text2 = font.render('You DEADED NOOB Score: ' + str(game.get_score()), True, (128, 0, 0))
            game.screen.fill("black")
            textRect = text2.get_rect()
            textRect.center = (X // 2, Y // 2)
            game.screen.blit(text2, textRect)
            pygame.display.update()
            pygame.time.delay(2000)
            break
            
        
                    

if __name__=="__main__":
    main()
