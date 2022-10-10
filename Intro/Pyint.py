'''
Created on 18 Apr 2022

@author: evane
'''

import pygame
import os


width, height = 800, 600

FPS = 60

GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Something Random")
PICTURE = pygame.image.load(os.path.join('resources', 'pic1.png'))
SONG = os.path.join(os.getcwd(), 'resources/song1.mp3')





def draw_fn():
    GScreen.fill((255, 0, 255))
    GScreen.blit(PICTURE, (0, 0))
    
    pygame.display.update()
    

def main():
    
    pygame.mixer.init()
    pygame.mixer.music.load(SONG)
    pygame.mixer.music.play(-1)
    
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                
        draw_fn()
                
        
                
                
if __name__ == "__main__":
    main()