# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    ## PYGAME VARS
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
     ## GROUPS 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    ## PLAYER VARS
    Player.containers = (drawable, updatable)
    player = Player((SCREEN_WIDTH/2, SCREEN_HEIGHT/2), PLAYER_RADIUS)
    
    Shot.containers = (drawable, updatable)
    

    dt = 0
   
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for obj in asteroids:
            if obj.collision_detection(player):
                print("Game Over")
                return
          
        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)
                   
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__== "__main__":
    main()