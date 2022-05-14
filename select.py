import pygame, sys, json
import run
import main2
import button
import skin

def main():
	def buttons_draw(screen):
		for b in buttons:
			b.draw(screen)

	pygame.init()
	pygame.mixer.music.stop()

	pygame.display.set_caption('NekoDarkLand')	#window title
	clock = pygame.time.Clock()		#FPS

	text_font = pygame.font.Font(None, 60)	#Text Font

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
	#skin button position
	w = WIDTH-(WIDTH-40)
	h = HEIGHT-80

	#button
	back_button = button.Button('Back', 200, 40, (w_center_200, h_bottom+100), 5)
	skin_button = button.Button('Skin', 100, 40, (w, h), 5)
	buttons.append(back_button)
	buttons.append(skin_button)

	def img():
		with open("data.json", "r") as f:	#config size screen
			data = json.load(f)
			map1 = data["unlock"][0]["map1"]
			map2 = data["unlock"][0]["map2"]
			map3 = data["unlock"][0]["map3"]
			map4 = data["unlock"][0]["map4"]
			map5 = data["unlock"][0]["map5"]
			map6 = data["unlock"][0]["map6"]
		#image level (button)
		if map1 == "True":
			level_1 = pygame.image.load(r'./level-image/1.png')	#image level 1
		else:
			level_1 = pygame.image.load(r'./level-image/1_lock.png')	#image level 1
		if map2 == "True":
			level_2 = pygame.image.load(r'./level-image/2.png')	#image level 2
		else:
			level_2 = pygame.image.load(r'./level-image/2_lock.png')	#image level 2
		if map3 == "True":
			level_3 = pygame.image.load(r'./level-image/3.png')	#image level 3
		else:
			level_3 = pygame.image.load(r'./level-image/3_lock.png')	#image level 3
		if map4 == "True":
			level_4 = pygame.image.load(r'./level-image/4.png')	#image level 4
		else:
			level_4 = pygame.image.load(r'./level-image/4_lock.png')	#image level 4
		if map5 == "True":
			level_5 = pygame.image.load(r'./level-image/5.png')	#image level 5
		else:
			level_5 = pygame.image.load(r'./level-image/5_lock.png')	#image level 5
		if map6 == "True":
			level_6 = pygame.image.load(r'./level-image/6.png')	#image level 6
		else:
			level_6 = pygame.image.load(r'./level-image/6_lock.png')	#image level 6
		#show | load image lock and unlock
		screen.blit(bg, (0, 0))
		screen.blit(level_1, (w1, h1))
		screen.blit(level_2, (w2, h1))
		screen.blit(level_3, (w3, h1))
		screen.blit(level_4, (w1, h2))
		screen.blit(level_5, (w2, h2))
		screen.blit(level_6, (w3, h2))

	# Text
	white = (255,255,255)
	text = text_font.render('Select level', True, white)
	# create a rectangular object for the text
	textRect = text.get_rect()
	textRect.center = (wt, ht)

	# transform bg size for every screen
	if WIDTH == 1920 or FULL == "True":		#for 1920x1080 and Fullscreen
		bg = pygame.transform.scale(bg, (1920, 1080))
	elif WIDTH == 1280 and FULL == "None":	#for 1280x720
		bg = pygame.transform.scale(bg, (1280, 720))
	elif WIDTH == 1000 and FULL == "None":	#for 1000x600
		bg = pygame.transform.scale(bg, (1000, 600))
						
	while True:
		img()	#show level image
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:	#Check click button and react
					with open("data.json", "r") as f:	#config size screen
						data = json.load(f)
						map1 = data["unlock"][0]["map1"]
						map2 = data["unlock"][0]["map2"]
						map3 = data["unlock"][0]["map3"]
						map4 = data["unlock"][0]["map4"]
						map5 = data["unlock"][0]["map5"]
						map6 = data["unlock"][0]["map6"]
					if map1 == "True":	#verif unlock level
						if w1 <= mouse[0] <= w1+200 and h1 <= mouse[1] <= h1+113:	#verif click level
							main2.main(1)	#run level
					if map2 == "True":	#verif unlock level
						if w2 <= mouse[0] <= w2+200 and h1 <= mouse[1] <= h1+113:	#verif click level
							main2.main(2)	#run level
					if map3 == "True":	#verif unlock level
						if w3 <= mouse[0] <= w3+200 and h1 <= mouse[1] <= h1+113:	##verif click level
							main2.main(3)	#run level
					if map4 == "True":	#verif unlock level
						if w1 <= mouse[0] <= w1+200 and h2 <= mouse[1] <= h2+113:	#verif click level
							main2.main(4)	#run level
					if map5 == "True":	#verif unlock level
						if w2 <= mouse[0] <= w2+200 and h2 <= mouse[1] <= h2+113:	#verif click level
							main2.main(5)	#run level
					if map6 == "True":	#verif unlock level
						if w3 <= mouse[0] <= w3+200 and h2 <= mouse[1] <= h2+113:	#verif click level
							main2.main(6)	#run level
					if w <= mouse[0] <= w+100 and h <= mouse[1] <= h+40:	#verif click skin button
						skin.main()	#skin redirect
					if w_center_200 <= mouse[0] <= w_center_200+200 and h_bottom+100-10 <= mouse[1] <= h_bottom+150:	#Back
						run.main()

		buttons_draw(screen)	#show button
		screen.blit(text, textRect)	#show text
		
		mouse = pygame.mouse.get_pos() # get mouse position
		clock.tick(60)	#fps
		pygame.display.update()

if __name__ == "__main__":
	main()