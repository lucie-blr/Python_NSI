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
	h_bottom = HEIGHT*(2/3)			#height bottom

	#button position
	if WIDTH == 1920 or FULL == "True":		#for 1920x1080 screen
		w1= WIDTH-((7/8)*WIDTH)					#first column
		w2= WIDTH/2-100							#second column
		w3= WIDTH-((2/8)*WIDTH)					#third column
		h1 = HEIGHT-(HEIGHT-150)				#First lign
		h2 = HEIGHT-(HEIGHT-350)				#second line
		wt, ht = WIDTH/2, HEIGHT-(HEIGHT-70)	#text position (select level)
	elif WIDTH == 1280:						#for 1280x720 screen
		w1= WIDTH-((7/8)*WIDTH)					#first column
		w2= WIDTH/2-100							#second column
		w3= WIDTH-((2/8)*WIDTH)					#third column
		h1 = HEIGHT-(HEIGHT-150)				#First lign
		h2 = HEIGHT-(HEIGHT-350)				#second line
		wt, ht = WIDTH/2, HEIGHT-(HEIGHT-70)	#text position (select level)
	elif WIDTH == 1000:						#for 1000x600 screen
		w1= WIDTH-((7/8)*WIDTH)					#first column
		w2= WIDTH/2-100							#second column
		w3= WIDTH-((2/8)*WIDTH)					#third column
		h1 = HEIGHT-(HEIGHT-150)				#First lign
		h2 = HEIGHT-(HEIGHT-350)				#second line
		wt, ht = WIDTH/2, HEIGHT-(HEIGHT-70)	#text position (select level)

	#button
	back_button = Button('Back', 200, 40, (w_center_200, h_bottom+100), 5)

	def img():
		#image level (button)
		level_1 = pygame.image.load(r'./level-image/1.png')	#image level 1
		level_2 = pygame.image.load(r'./level-image/2.png')	#image level 1
		level_3 = pygame.image.load(r'./level-image/3.png')	#image level 1
		level_4 = pygame.image.load(r'./level-image/4.png')	#image level 1
		level_5 = pygame.image.load(r'./level-image/5.png')	#image level 1
		level_6 = pygame.image.load(r'./level-image/6.png')	#image level 1
		#show
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
					if w1 <= mouse[0] <= w1+200 and h1 <= mouse[1] <= h1+113:	#1920
						main2.main(1)
					if w2 <= mouse[0] <= w2+200 and h1 <= mouse[1] <= h1+113:	#1920
						main2.main(2)
					if w3 <= mouse[0] <= w3+200 and h1 <= mouse[1] <= h1+113:	#1920
						main2.main(3)
					if w1 <= mouse[0] <= w1+200 and h2 <= mouse[1] <= h2+113:	#1920
						main2.main(4)
					if w2 <= mouse[0] <= w2+200 and h2 <= mouse[1] <= h2+113:	#1920
						main2.main(5)
					if w3 <= mouse[0] <= w3+200 and h2 <= mouse[1] <= h2+113:	#1920
						main2.main(6)
					if w_center_200 <= mouse[0] <= w_center_200+200 and h_bottom+100-10 <= mouse[1] <= h_bottom+150:	#Back
						run.main()

		buttons_draw()	#show button
		screen.blit(text, textRect)	#show text
		
		mouse = pygame.mouse.get_pos() # get mouse position
		clock.tick(60)	#fps
		pygame.display.update()

if __name__ == "__main__":
	main()