'''
Created on 8 Jun 2022

@author: evane
'''

import pygame
import random



class Food(pygame.sprite.Sprite): #sprite is an object that should be displayed on our screen
    def __init__(self, images_dict, selected_key, screensize, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.screensize = screensize
        self.image = images_dict[selected_key] #This is how we will change the images
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect() #gets the rectangler of the image
        self.rect.left, self.rect.bottom = random.randint(20, screensize[0]-20), -10
        self.speed =random.randrange(5, 10)
        self.score = 1 if selected_key == 'gold' else 5 #how much score you get for picking up a cookie or else(apple)
        
        
    def update(self):
        self.rect.bottom += self.speed
        if self.rect.top > self.screensize[1]:
            return True
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        