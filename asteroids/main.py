import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group() 

    Player.containers = (updatable, drawable)

    # create a player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            screen.fill("black")
            for item in drawable:
                item.draw(screen)
            pygame.display.flip()

        dt = clock.tick(60) / 1000
        updatable.update(dt)



if __name__ == "__main__":
    main()
