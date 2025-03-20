import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)



    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    running = True
    while running:
        dt = clock.tick(60)/1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        updatable.update(dt)
        
        # Rendering
        screen.fill((0,0,0))
        
        for entities in drawable:
            entities.draw(screen)
        pygame.display.flip()
        
    

if __name__ == "__main__":
    main()