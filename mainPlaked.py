# -*- coding: utf-8 -*-
# @Author: Amar Prakash Pandey
# @Date:   2016-06-04
# @Email:  amar.om1994@gmail.com  
# @Github username: @amarlearning
# @Last Modified by: Amar Prakash Pandey  
# @Last Modified date: 2016-06-20
# MIT License. You can find a copy of the License
# @http://amarlearning.mit-license.org

# import library here
import pygame
import time

# game initialization done
pygame.init()

# game display changed
gameDisplay = pygame.display.set_mode((800,600))

# game name init and display updated
pygame.display.set_caption('Placked | Beyond the Universe')
pygame.display.update()

# variable init 
gameExit = False

while not gameExit :
	for event in pygame.event.get():
		if event.type  == pygame.QUIT:
			gameExit = True

pygame.quit()
# you can signoff now, everything looks good!
quit()
