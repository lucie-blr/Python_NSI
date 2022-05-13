import pygame
import json
import sys
import button
from player import Player
import run
from settings import import_folder

def main():
	def buttons_draw(screen):
		for b in buttons:
			b.draw(screen)

	pygame.init()

	pygame.display.set_caption('NekoDarkLand')	#window title
	clock = pygame.time.Clock()		#FPS

	text_font = pygame.font.Font(None, 60)	#Text Font
	text_font2 = pygame.font.Font(None, 30)	#Text Font for coin text

	bg = pygame.image.load(r'bg.gif')	# background annimation

	buttons = []

	with open("data.json", "r") as f:	#config size screen
		data = json.load(f)
		WIDTH = data["WIDTH"]
		HEIGHT = data["HEIGHT"]
		FULL = data["FULL"]

	if FULL == "None":	
		screen = pygame.display.set_mode((WIDTH, HEIGHT))
	else:
		screen = pygame.display.set_mode()
		WIDTH, HEIGHT = screen.get_size()

	# button position
	w_center_200 = (WIDTH/2)-100	#widht for 200px button, center
	h_bottom = HEIGHT*(2/3)			#height bottom

	#for level button
	w1= WIDTH-((7/8)*WIDTH)					#first column
	w2= WIDTH/2-100							#second column
	w3= WIDTH-((2/8)*WIDTH)					#third column
	h1 = HEIGHT-(HEIGHT-150)				#First lign
	h2 = HEIGHT-(HEIGHT-350)				#second line
	wt, ht = WIDTH/2, HEIGHT-(HEIGHT-70)	#text position (select level)

	#button
	back_button = button.Button('Back', 200, 40, (w_center_200, h_bottom+100), 5)
	buttons.append(back_button)

	frame_index = 0

	def skin(frame_index):
		with open("data.json", "r") as f:	#config size screen
			data = json.load(f)


		full_path = './alien/red/idle'
		animations = import_folder(full_path)
		frame_index += 0.15 #Ajout au numéro de frame la vitesse d'animation
		if frame_index >= len(animations): #si le numéro de frame est supérieur ou égale à la taille de la liste d'image
			frame_index = 0 #le numéro d'image vaut 0
		image = animations[int(frame_index)] #défini l'image à l'arrondi du numéro d'image
		

		screen.blit(bg, (0, 0))
		screen.blit(image, (200, 200))
		return frame_index

	# Text
	white = (255,255,255)
	with open("data.json", "r") as f:
		data = json.load(f)
		coin = data["coin"]
	text = text_font.render('Buy Skin', True, white)
	text2 = text_font2.render(f'Coins : {coin}', True, white)
	# create a rectangular object for the text
	textRect = text.get_rect()
	textRect2 = text2.get_rect()
	textRect.center = (wt, ht)
	textRect2.center = (WIDTH - (WIDTH-200) , HEIGHT - (HEIGHT-40))

	# transform bg size for every screen
	if WIDTH == 1920 or FULL == "True":		#for 1920x1080 and Fullscreen
		bg = pygame.transform.scale(bg, (1920, 1080))
	elif WIDTH == 1280 and FULL == "None":	#for 1280x720
		bg = pygame.transform.scale(bg, (1280, 720))
	elif WIDTH == 1000 and FULL == "None":	#for 1000x600
		bg = pygame.transform.scale(bg, (1000, 600))
						
	while True:
		frame_index = skin(frame_index)	#show level image
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:	#Check click button and react

					if w_center_200 <= mouse[0] <= w_center_200+200 and h_bottom+100-10 <= mouse[1] <= h_bottom+150:	#Back
						run.main()

		buttons_draw(screen)	#show button
		screen.blit(text, textRect)	#show text
		screen.blit(text2, textRect2)	#show coin text
		
		mouse = pygame.mouse.get_pos() # get mouse position
		clock.tick(60)	#fps
		pygame.display.update()

if __name__ == "__main__":
	main()