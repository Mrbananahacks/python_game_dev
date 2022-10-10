'''
Created on 18 Aug 2022

@author: evane
'''

import os 

SCREENSIZE= (956, 560)

FONTPATH = os.path.join(os.getcwd(), 'resources/font/simkai.ttf')

IMAGEPATHS = {
    'asteroid': os.path.join(os.getcwd(), 'resources/images/asteroid.png'),
    'bg_big': os.path.join(os.getcwd(), 'resources/images/bg_big.png'),
    'bullet': os.path.join(os.getcwd(), 'resources/images/bullet.png'),
    'seamless_space': os.path.join(os.getcwd(), 'resources/images/seamless_space.png'),
    'ship_exploded': os.path.join(os.getcwd(), 'resources/images/ship_exploded.png'),
    'ship': os.path.join(os.getcwd(), 'resources/images/ship.png'),
    'space3': os.path.join(os.getcwd(), 'resources/images/space3.jpg')
}