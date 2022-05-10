import pygame, sys, json
import run
import main2

def main():
	class Button:
		def __init__(self,text, width, height, pos, elevation):
			#Core attributes 
			self.pressed = False
			self.elevation = elevation
			self.dynamic_elecation = elevation
			self.original_y_pos = pos[1]

			# top rectangle 
			self.top_rect = pygame.Rect(pos, (width, height))
			self.top_color = '#015E5E'

			# bottom rectangle 
			self.bottom_rect = pygame.Rect(pos, (width, height))
			self.bottom_color = '#014A4A'
			#text
			self.text = text
			self.text_surf = gui_font.render(text, True, '#FFFFFF')
			self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
			buttons.append(self)

		def change_text(self, newtext):
			self.text_surf = gui_font.render(newtext, True, '#FFFFFF')
			self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

		def draw(self):
			# elevation logic 
			self.top_rect.y = self.original_y_pos - self.dynamic_elecation
			self.text_rect.center = self.top_rect.center 

			self.bottom_rect.midtop = self.top_rect.midtop
			self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

			pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
			pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
			screen.blit(self.text_surf, self.text_rect)
			self.check_click()

		def check_click(self):
			mouse = pygame.mouse.get_pos()
			if self.top_rect.collidepoint(mouse):
				self.top_color = '#02DADA'
				if pygame.mouse.get_pressed()[0]:
					self.dynamic_elecation = 0
					self.pressed = True
					self.change_text(f"{self.text}")
				else:
					self.dynamic_elecation = self.elevation
					if self.pressed == True:
						self.pressed = False
						self.change_text(self.text)
					
			else:
				self.dynamic_elecation = self.elevation
				self.top_color = '#015E5E'

	def buttons_draw():
		for b in buttons:
			b.draw()

	pygame.init()

	pygame.display.set_caption('NekoDarkLand')	#window title
	clock = pygame.time.Clock()		#FPS

	gui_font = pygame.font.Font(None, 30)	#Font
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
	w_center_150 = (WIDTH/2)-75		#widht for 150px button, center

	h_center = HEIGHT/2				#height center
	h_bottom = HEIGHT*(2/3)			#height bottom

	#button
	button_1 = Button('Level 1', 150, 40, (w_center_150-170, h_center), 5)
	button_2 = Button('Level 2', 150, 40, (w_center_150, h_center), 5)
	button_3 = Button('Level 3', 150, 40, (w_center_150+170, h_center), 5)
	button_4 = Button('Level 4', 150, 40, (w_center_150, h_bottom-50), 5)
	button_5 = Button('Level 5', 150, 40, (w_center_150, h_bottom-50), 5)
	button_6 = Button('Level 6', 150, 40, (w_center_150, h_bottom-50), 5)
	back_button = Button('Back', 200, 40, (w_center_200, h_bottom+100), 5)

	# Text
	white = (255,255,255)
	text = text_font.render('sheeesh', True, white)
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
						pygame.quit()
						run.main()
					if w_center_150 <= mouse[0] <= w_center_150+150 and h_center-10 <= mouse[1] <= h_center+50: 		#1280
						pygame.quit()
						run.main()
					if w_center_150+170 <= mouse[0] <= w_center_150+170+150 and h_center-10 <= mouse[1] <= h_center+50: #1000
						pygame.quit()
						run.main()
					if w_center_150 <= mouse[0] <= w_center_150+150 and h_bottom-50-10 <= mouse[1] <= h_bottom-50+50:	#Fullscreen
						pygame.quit()
						run.main()
					if w_center_200 <= mouse[0] <= w_center_200+200 and h_bottom+100-10 <= mouse[1] <= h_bottom+150:	#Back
						run.main()

		buttons_draw()	#show button
		screen.blit(text, textRect)	#show text
		
		mouse = pygame.mouse.get_pos() # get mouse position
		clock.tick(60)	#fps
		pygame.display.update()

if __name__ == "__main__":
	main()