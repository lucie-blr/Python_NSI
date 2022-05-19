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

	with open("data.json", "r") as f:
		data = json.load(f)
		WIDTH = data["WIDTH"]
		HEIGHT = data["HEIGHT"]
		FULL = data["FULL"]
		caption = data["caption"]
	pygame.display.set_caption(caption)	#window title
	clock = pygame.time.Clock()		#FPS

	text_font = pygame.font.Font(None, 60)	#Text Font
	text_font2 = pygame.font.Font(None, 30)	#Text Font for coin text

	bg = pygame.image.load(r'bg.gif')	# background annimation
	cash_iamge = pygame.image.load(r'./alien/cash.png')

	buttons = []


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
	with open("data.json", "r") as f:	#config size screen
		data = json.load(f)
		s1 = data["skin"]["1"]
		s2 = data["skin"]["2"]
		s3 = data["skin"]["3"]
		s4 = data["skin"]["4"]
		s5 = data["skin"]["5"]
		s6 = data["skin"]["6"]
		print(s1)
		print(s2)
		print(s3)
	if s1 == "True":	#verif skin dispo
		buy1_button = button.Button('Select', 200, 40, (w1, h1), 5)
	else:
		buy1_button = button.Button('Buy for 0', 200, 40, (w1, h1), 5)
	if s2 == "True":	#verif skin dispo
		buy2_button = button.Button('Select', 200, 40, (w2, h1), 5)
	else:
		buy2_button = button.Button('Buy for 20', 200, 40, (w2, h1), 5)
	if s3 == "True":	#verif skin dispo
		buy3_button = button.Button('Select', 200, 40, (w3, h1), 5)
	else:
		buy3_button = button.Button('Buy for 40', 200, 40, (w3, h1), 5)
	if s4 == "True":	#verif skin dispo
		buy4_button = button.Button('Select', 200, 40, (w1, h2), 5)
	else:
		buy4_button = button.Button('Buy for 60', 200, 40, (w1, h2), 5)
	if s5 == "True":	#verif skin dispo
		buy5_button = button.Button('Select', 200, 40, (w2, h2), 5)
	else:
		buy5_button = button.Button('Buy for 100', 200, 40, (w2, h2), 5)
	if s6 == "True":	#verif skin dispo
		buy1_button = button.Button('Select', 200, 40, (w3, h2), 5)
	else:
		buy6_button = button.Button('Buy for 150', 200, 40, (w3, h2), 5)

	back_button = button.Button('Back', 200, 40, (w_center_200, h_bottom+100), 5)
	#use class button 
	buttons.append(buy1_button)
	buttons.append(buy2_button)
	buttons.append(buy3_button)
	buttons.append(buy4_button)
	buttons.append(buy5_button)
	buttons.append(buy6_button)
	buttons.append(back_button)

	frame_index = 0
	frame_index2 = 0

	def skin(frame_index, frame_index2):
		with open("data.json", "r") as f:	#config size screen
			data = json.load(f)


		full_path = './alien/red/idle'
		animations = import_folder(full_path)
		frame_index += 0.15 #Ajout au numéro de frame la vitesse d'animation
		if frame_index >= len(animations): #si le numéro de frame est supérieur ou égale à la taille de la liste d'image
			frame_index = 0 #le numéro d'image vaut 0
		image = animations[int(frame_index)] #défini l'image à l'arrondi du numéro d'image

		full_path2 = './alien/blue/idle'
		animations = import_folder(full_path2)
		frame_index2 += 0.15 #Ajout au numéro de frame la vitesse d'animation
		if frame_index2 >= len(animations): #si le numéro de frame est supérieur ou égale à la taille de la liste d'image
			frame_index2 = 0 #le numéro d'image vaut 0
		image2 = animations[int(frame_index2)] #défini l'image à l'arrondi du numéro d'image
		

		screen.blit(bg, (0, 0))
		screen.blit(image, (w1+75, h1+75))
		screen.blit(image2, (w2+75, h1+75))
		return frame_index, frame_index2

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

	def coin_load():
		cash_image = pygame.image.load(r'./alien/cash.png')	#image for coin
		t = len(str(coin))
		if t <= 99:
			w_coin_total = 70
			h_coin_total = 70
		if t <= 999:
			w_coin_total = 70
			h_coin_total = 70
		if t <= 9999:
			w_coin_total = 70
			h_coin_total = 70
		else:
			w_coin_total = 70
			h_coin_total = 70
		cash_image_total = pygame.transform.scale(cash_image, (25, 25))
		screen.blit(cash_image_total, (w_coin_total, h_coin_total))
		#coin img position
		# w_coin = w1
		# h_coin = h1
		# for i in range(2):
		# 	for i in range(3):
		# 		screen.blit(cash_image_total, (w_coin+165, h_coin))
		# 		w_coin = w2
		# 	h_coin = h2

	while True:
		frame_index, frame_index2 = skin(frame_index, frame_index2)	#show skin
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:	#Check click button and react

					if w_center_200 <= mouse[0] <= w_center_200+200 and h_bottom+100-10 <= mouse[1] <= h_bottom+150:	#Back
						run.main()

					if w1 <= mouse[0] <= w1+200 and h1-10 <= mouse[1] <= h1+30:	#Back
						if s1 == "True":
							print("p")
						elif coin >=0 and s1 == "None":
							with open("data.json", "r") as t:	#open and read
								data = json.load(t)
							data["skin"]["1"] = "True"
							data["coin"] -= 0
							with open("data.json", "w") as f:	#add skin
								json.dump(data,f)
					if w2 <= mouse[0] <= w2+200 and h1-10 <= mouse[1] <= h1+30:	#Back
						if s2 == "True":
							print("p")
						elif coin >=20 and s1 == "None":
							data["coin"] -= 0
							with open("data.json", "r") as t:	#open and read
								data = json.load(t)
							data["skin"]["2"] = "True"
							data["coin"] -= 20
							with open("data.json", "w") as f:	#add skin
								json.dump(data,f)
					if w3 <= mouse[0] <= w3+200 and h1-10 <= mouse[1] <= h1+30:	#Back
							if s3 == "True":
								print("p")
							elif coin >=40 and s3 == "None":
								data["coin"] -= 0
								with open("data.json", "r") as t:	#open and read
									data = json.load(t)
								data["skin"]["3"] = "True"
								data["coin"] -= 40
								with open("data.json", "w") as f:	#add skin
									json.dump(data,f)
					if s4 == "True" or coin >=60:
						if w1 <= mouse[0] <= w1+200 and h2-10 <= mouse[1] <= h2+30:	#Back
							print("p")
					if s5 == "True" or coin >=100:
						if w2 <= mouse[0] <= w2+200 and h2-10 <= mouse[1] <= h2+30:	#Back
							print("p")
					if s6 == "True" or coin >=150:
						if w3 <= mouse[0] <= w3+200 and h2-10 <= mouse[1] <= h2+30:	#Back
							print("p")
					

		buttons_draw(screen)	#show button
		screen.blit(text, textRect)	#show text
		screen.blit(text2, textRect2)	#show coin text
		coin_load()
		
		mouse = pygame.mouse.get_pos() # get mouse position
		clock.tick(60)	#fps
		pygame.display.update()

if __name__ == "__main__":
	main()