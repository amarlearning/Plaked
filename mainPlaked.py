# -*- coding: utf-8 -*-
# @Author: Amar Prakash Pandey
# @Date:   2016-06-04
# @Email:  amar.om1994@gmail.com  
# @Github username: @amarlearning
# @Last Modified by: Amar Prakash Pandey  
# @Last Modified date: 2016-07-18
# MIT License. You can find a copy of the License
# @http://amarlearning.mit-license.org

# import library here
import pygame
import time
import random
from os import path

# contant value initialised
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

# display init
display_width = 800
display_height = 600

# game initialization done
pygame.init()
pygame.mixer.init()

# path for the image folder
assets = path.join(path.dirname(__file__), 'assets')
sound_folder = path.join(path.dirname(__file__), 'sounds')

# game display changed
gameDisplay = pygame.display.set_mode((display_width, display_height))

# image loading for both apple and snake
snakeimg = pygame.image.load(path.join(assets + '/snake.png'))
snakebody = pygame.image.load(path.join(assets + '/body.png'))
snaketail = pygame.image.load(path.join(assets + '/tail.png'))
gameicon = pygame.image.load(path.join(assets + '/gameicon.png'))
appleimg = pygame.image.load(path.join(assets + '/apple.png'))
coverimg = pygame.image.load(path.join(assets + '/coverimage.png'))
coverimg = pygame.transform.scale(coverimg,(800,600))

# game name init and display updated
pygame.display.set_caption('Placked | Beyond the Apple')
pygame.display.update()

# updating the game icon in window
pygame.display.set_icon(gameicon)

# controling the no. of frames per sec uisng pygame clock
clock = pygame.time.Clock()

# Frames per second 
FPS = 10

# moving block size
block = 20
appleSize = 30

# snake image direction variable
direction = "right"

# init font object with font size 25 
smallfont = pygame.font.SysFont("comicsansms", 20)
medfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 70)

# function to pause the game
def pause():
	paused = True
	menu_song = pygame.mixer.music.load(path.join(sound_folder, "menu.ogg"))
	pygame.mixer.music.play(-1)
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.QUIT()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
					pygame.mixer.music.fadeout(400)
				if event.key == pygame.K_q:
					pygame.QUIT()
					quit()
		gameDisplay.fill(white)
		message_to_display("Paused", black, -80, "large")
		message_to_display("Press [C] to Continue and [Q] to Quit!", black)
		pygame.display.update()


# function to print score
def score(score):
	text = smallfont.render("Score : " + str(score), True, black)
	gameDisplay.blit(text, [2,2])


# function for random apple generation
def randomAppleGen():
	randomFruitX = round(random.randrange(0, display_width - appleSize) / 10.0) * 10.0
	randomFruitY = round(random.randrange(0, display_height - appleSize) / 10.0) * 10.0

	return randomFruitX, randomFruitY

# function for start screen!
def start_screen():
	menu_song = pygame.mixer.music.load(path.join(sound_folder, "menu.ogg"))
	pygame.mixer.music.play(-1)

	# titleTrack.play()
	show_the_welcome_screen = True
	while show_the_welcome_screen:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					show_the_welcome_screen = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()

		gameDisplay.fill(white)
		gameDisplay.blit(coverimg, (0,0))
		message_to_display("Plaked", green, -120, "large")
		message_to_display("The objective of this game is to eat red apples", black, -30)
		message_to_display("The more apple you eat, the longer you get", black, 10)
		message_to_display("If you run into yourself, or the boundary, you die!", black, 50)
		message_to_display("Press [C] to Play, [P] to Pause and [Q] to Quit", black, 150)

		pygame.display.update()
		clock.tick(15)


# to generate and update snake :P
def snake(block, snakeList):
	# At some point, we may want to rotate the snake's body when it reaches
	# a part where the snake turns
	body = pygame.transform.rotate(snakebody, 0)
	tail = pygame.transform.rotate(snaketail, 0)
	
	if direction == "right":
		head = pygame.transform.rotate(snakeimg, 270)

	if direction == "left":
		head = pygame.transform.rotate(snakeimg, 90)

	if direction == "up":
		head = snakeimg

	if direction == "down":
		head = pygame.transform.rotate(snakeimg, 180)


	# This method is just working, but not good.
	# Will have to hamake it better and add the snake tail as well.
	gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
	for XnY in snakeList[:-1]:
		# gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
		pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block, block])


def text_object(msg, color,size):
	if size == "small":	
		textSurface = smallfont.render(msg, True, color)
		return textSurface, textSurface.get_rect()

	if size == "medium":
		textSurface = medfont.render(msg, True, color)
		return textSurface, textSurface.get_rect()

	if size == "large":
		textSurface = largefont.render(msg, True, color)
		return textSurface, textSurface.get_rect()

# func to print message on game display
def message_to_display(msg, color, y_displace = 0, size = "small"):
	textSurf , textRect = text_object(msg, color, size)
	textRect.center = (display_width/2), (display_height/2) + y_displace
	gameDisplay.blit(textSurf, textRect)


# game starts here
def gameLoop():
	# global variable direction
	global direction
	global isDead

	# menu sound stops
	pygame.mixer.music.fadeout(600)
	
	direction = "right"

	# variable init 
	gameExit = False
	gameOver = False
	isDead = False

	# snake variables
	snakeList = []
	snakeLength = 1

	randomFruitX, randomFruitY = randomAppleGen()

	start_x = display_width/2
	start_y = display_height/2
	
	move_to_h = 10
	move_to_v = 0

	while not gameExit :
		if gameOver == True:
			menu_song = pygame.mixer.music.load(path.join(sound_folder, "gameover.ogg"))
			pygame.mixer.music.play(-1)

			while gameOver == True :
				gameDisplay.fill(white)
				message_to_display("Game Over", red, -70, "large")
				text = smallfont.render("Your final score is : " + str(snakeLength), True, black)
				gameDisplay.blit(text, [300,300])
				message_to_display("Press [C] to Play Again and [Q] to quit!", black, 60)
				pygame.display.update()

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						gameOver = False
						gameExit = True
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
				if event.key == pygame.K_LEFT and move_to_h == 0:
					direction = "left"
					move_to_h = -block
					move_to_v = 0
				elif event.key == pygame.K_RIGHT and move_to_h == 0:
					direction = "right"
					move_to_h = block
					move_to_v = 0
				elif event.key == pygame.K_UP and move_to_v == 0:
					direction = "up"
					move_to_v = -block
					move_to_h = 0
				elif event.key == pygame.K_DOWN and move_to_v == 0:
					direction = "down"
					move_to_v = block
					move_to_h = 0
				elif event.key == pygame.K_p:
					pause()
					
		if start_x >= display_width or start_x < 0 or start_y >= display_height or start_y < 0:
			gameOver = True

		start_x += move_to_h
		start_y += move_to_v

		gameDisplay.fill(white)
		gameDisplay.blit(appleimg, (randomFruitX, randomFruitY))

		snakeHead = []
		snakeHead.append(start_x)
		snakeHead.append(start_y)
		snakeList.append(snakeHead)

		if len(snakeList) > snakeLength:
			del snakeList[0]

		score(snakeLength - 1)

		snake(block, snakeList)
		pygame.display.update()

		# to see if snake has eaten himself or not
		for eachSegment in snakeList[:-1]:
			if eachSegment == snakeHead:
				isDead = True
				snake(block, snakeList)
				pygame.time.delay(1000)
				gameOver = True

		if start_x > randomFruitX and start_x < randomFruitX + appleSize or start_x + block > randomFruitX and start_x + block < randomFruitX + appleSize:
			if start_y > randomFruitY and start_y < randomFruitY + appleSize:
				randomFruitX, randomFruitY = randomAppleGen()
				snakeLength += 1 
				menu_song = pygame.mixer.music.load(path.join(sound_folder, "wakka.ogg"))
				pygame.mixer.music.play(0)
			if start_y + block > randomFruitY and start_y + block < randomFruitY + appleSize:
				randomFruitX, randomFruitY = randomAppleGen()
				snakeLength += 1 
				menu_song = pygame.mixer.music.load(path.join(sound_folder, "wakka.ogg"))
				pygame.mixer.music.play(0)

		# initialising no. of frames per sec
		clock.tick(FPS)


	pygame.quit()
	# you can signoff now, everything looks good!
	quit()

# # this fuction kicks-off everything 
start_screen()
gameLoop()
