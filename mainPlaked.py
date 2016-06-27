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

# contant value initialised
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

# game initialization done
pygame.init()

# game display changed
gameDisplay = pygame.display.set_mode((800,600))

# game name init and display updated
pygame.display.set_caption('Placked | Beyond the Universe')
pygame.display.update()

# controling the no. of frames per sec uisng pygame clock
clock = pygame.time.Clock()

# variable init 
gameExit = False
start_x = 400
start_y = 300
move_to_h = 0
move_to_v = 0

while not gameExit :
	for event in pygame.event.get():
		if event.type  == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				move_to = -10
			if event.key == pygame.K_RIGHT:
				move_to = 10

	start_x += move_to

	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [start_x, start_y , 10, 10])
	pygame.display.update()

	# initialising no. of frames per sec
	clock.tick(10)

pygame.quit()
# you can signoff now, everything looks good!
quit()
