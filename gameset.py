import pygame, sys, json
import run
import button

def main():
	def buttons_draw(screen):
		for b in buttons:
			b.draw(screen)

	pygame.init()

	pygame.display.set_caption('RedHoodDarkLand')	#window title
	clock = pygame.time.Clock()		#FPS

	text_font = pygame.font.Font('./font/Amatic_SC/AmaticSC-Bold.ttf', 40) #text font

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
	w_center_150 = (WIDTH/2)-75		#widht for 150px button, center

	h_center = HEIGHT/2				#height center
	h_bottom = HEIGHT*(2/3)			#height bottom

	#button
	button_1920 = button.Button('1920x1080', 150, 40, (w_center_150-170, h_center), 5)
	button_1280 = button.Button('1280x720', 150, 40, (w_center_150, h_center), 5)
	button_1000 = button.Button('1000x600', 150, 40, (w_center_150+170, h_center), 5)
	button_full = button.Button('Fullscreen', 150, 40, (w_center_150, h_bottom-50), 5)
	back_button = button.Button('Back', 200, 40, (w_center_200, h_bottom+100), 5)
	buttons.append(button_1920)
	buttons.append(button_1280)
	buttons.append(button_1000)
	buttons.append(button_full)
	buttons.append(back_button)

	# Text
	white = (255,255,255)
	text = text_font.render('Chose screen size', True, white)
	# create a rectangular object for the text
	textRect = text.get_rect()
	textRect.center = (WIDTH // 2, HEIGHT-(HEIGHT-150))

	# transform bg size for every screen
	if WIDTH == 1920 or FULL == "True":		#for 1920x1080 and Fullscreen
		bg = pygame.transform.scale(bg, (1920, 1080))
	elif WIDTH == 1280 and FULL == "None":	#for 1280x720
		bg = pygame.transform.scale(bg, (1280, 720))
	elif WIDTH == 1000 and FULL == "None":	#for 1000x600
		bg = pygame.transform.scale(bg, (1000, 600))
						
	while True:
		screen.blit(bg, (0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:	#Check click button and react
					if w_center_150-170 <= mouse[0] <= w_center_150-170+150 and h_center-10 <= mouse[1] <= h_center+50:	#1920
						with open("data.json", "w") as f:	#config size screen
							data["WIDTH"] = 1920
							data["HEIGHT"] = 1080
							if FULL == "True":
								data["FULL"] = "None"
							json.dump(data,f)
						pygame.quit()
						run.main()
					if w_center_150 <= mouse[0] <= w_center_150+150 and h_center-10 <= mouse[1] <= h_center+50: 		#1280
						with open("data.json", "w") as f:	#config size screen
							data["WIDTH"] = 1280
							data["HEIGHT"] = 720
							if FULL == "True":
								data["FULL"] = "None"
							json.dump(data,f)
						pygame.quit()
						run.main()
					if w_center_150+170 <= mouse[0] <= w_center_150+170+150 and h_center-10 <= mouse[1] <= h_center+50: #1000
						with open("data.json", "w") as f:	#config size screen
							data["WIDTH"] = 1000
							data["HEIGHT"] = 600
							if FULL == "True":
								data["FULL"] = "None"
							json.dump(data,f)
						pygame.quit()
						run.main()
					if w_center_150 <= mouse[0] <= w_center_150+150 and h_bottom-50-10 <= mouse[1] <= h_bottom-50+50:	#Fullscreen
						with open("data.json", "w") as f:	#config size screen
							if FULL == "True":
								data["FULL"] = "None"
							else:
								data["FULL"] = "True"
							json.dump(data,f)
						pygame.quit()
						run.main()
					if w_center_200 <= mouse[0] <= w_center_200+200 and h_bottom+100-10 <= mouse[1] <= h_bottom+150:	#Back
						run.main()

		buttons_draw(screen)	#show button
		screen.blit(text, textRect)	#show text
		
		mouse = pygame.mouse.get_pos() # get mouse position
		clock.tick(60)	#fps
		pygame.display.update()

if __name__ == "__main__":
	main()