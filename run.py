import pygame, sys, json
import gameset
import select

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
	text_font = pygame.font.Font(None, 22)	#Text Font

	logo = pygame.image.load(r'logo.png')	#banner
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

	w = (WIDTH/2)-100
	h = HEIGHT*(2/3)

	# transform bg size for every screen
	if WIDTH == 1920 or FULL == "True":		#for 1920x1080 and Fullscreen
		bg = pygame.transform.scale(bg, (1920, 1080))
	elif WIDTH == 1280 and FULL == "None":	#for 1280x720
		bg = pygame.transform.scale(bg, (1280, 720))
	elif WIDTH == 1000 and FULL == "None":	#for 1000x600
		bg = pygame.transform.scale(bg, (1000, 600))

	#button
	button1 = Button('Play', 200, 40, (w, h), 5)	#play
	button2 = Button('Setting', 200, 40, (w, h+50), 5)	#settings
	button3 = Button('Exit', 200, 40, (w, h+100), 5)	#exit 

	# Text
	white = (255,255,255)
	text = text_font.render('v 1.0', True, white)
	# create a rectangular object for the text
	textRect = text.get_rect()
	textRect.center = (WIDTH-40 , HEIGHT-20)

	while True:
		screen.blit(bg, (0, 0))
		screen.blit(logo, ((WIDTH-906)/2, 200))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:	#Check click button and react
					if w <= mouse[0] <= w+200 and h-10 <= mouse[1] <= h+50:			#PLay
						select.main()
					if w <= mouse[0] <= w+200 and h+50-10 <= mouse[1] <= h+100:		#settings
						gameset.main()
					if w <= mouse[0] <= w+200 and h+100-10 <= mouse[1] <= h+150:	#exit
						pygame.quit()
						sys.exit()

		mouse = pygame.mouse.get_pos()	#get mouse position
		buttons_draw()	#show button
		screen.blit(text, textRect)	#show text

		clock.tick(60)	#fps
		pygame.display.update() 

if __name__ == "__main__":
	main()