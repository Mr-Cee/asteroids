# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    ## PYGAME VARS
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
     ## GROUPS 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
   
   
   
    ## PLAYER VARS
    player = Player((SCREEN_WIDTH/2, SCREEN_HEIGHT/2), PLAYER_RADIUS)

    
   
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__== "__main__":
    main()