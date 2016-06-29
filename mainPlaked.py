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
import random

# contant value initialised
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

# display init
display_width = 800
display_height = 600

# game initialization done
pygame.init()

# game display changed
gameDisplay = pygame.display.set_mode((display_width, display_height))

# game name init and display updated
pygame.display.set_caption('Placked | Beyond the Universe')
pygame.display.update()

# controling the no. of frames per sec uisng pygame clock
clock = pygame.time.Clock()

# Frames per second 
FPS = 10

# moving block size
block = 10

# init font object with font size 25 
font = pygame.font.SysFont("cursive", 25)

def message_to_display(msg, color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [display_width/2-200, display_height/2])

def gameLoop():
	# variable init 
	gameExit = False
	gameOver = False

	randomFruitX = round(random.randrange(0, display_width - block) / 10.0) * 10.0
	randomFruitY = round(random.randrange(0, display_height - block) / 10.0) * 10.0

	start_x = display_width/2
	start_y = display_height/2
	
	move_to_h = 0
	move_to_v = 0

	while not gameExit :

		while gameOver == True :
			gameDisplay.fill(white)
			message_to_display("Game Over, Press C to play again or Q to quit!", red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						gameLoop()


		for event in pygame.event.get():
			if event.type  == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					move_to_h = -block
					move_to_v = 0
				if event.key == pygame.K_RIGHT:
					move_to_h = block
					move_to_v = 0
				if event.key == pygame.K_UP:
					move_to_v = -block
					move_to_h = 0
				if event.key == pygame.K_DOWN:
					move_to_v = block
					move_to_h = 0
					
		if start_x >= display_width or start_x < 0 or start_y >= display_height or start_y < 0:
			gameOver = True

		start_x += move_to_h
		start_y += move_to_v

		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay, red, [randomFruitX, randomFruitY, block, block])
		pygame.draw.rect(gameDisplay, black, [start_x, start_y , block, block])
		pygame.display.update()

		# initialising no. of frames per sec
		clock.tick(FPS)


	pygame.quit()
	# you can signoff now, everything looks good!
	quit()

gameLoop()