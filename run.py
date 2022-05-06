import pygame, sys
from main2 import main

buttons = []

class Button:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
 
		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#015E5E'
 
		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#014A4A'
		#text
		self.text = text
		self.text_surf = gui_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
		buttons.append(self)
 
	def change_text(self, newtext):
		self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
 
	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 
 
		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
 
		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()
 
	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
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
    
def on_setting():
	print("sheeeeeeeeeesh2")


pygame.init()
pygame.display.set_caption('NekoDarkLand')
screen = pygame.display.set_mode((1200,700))
bg = pygame.image.load("./alien/background2.jpg")
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None,30)
logo = pygame.image.load(r'logo.png')

height = screen.get_height()
width = screen.get_width()
 
button1 = Button('Play',200,40,(500,500),5)
button2 = Button('Setting',200,40,(500,550),5)
button3 = Button('Exit',200,40,(500,600),5)


def buttons_draw():
	for b in buttons:
		b.draw()
 
while True:
	screen.blit(bg,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

  
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				if 500 <= mouse[0] <= 700 and 500 <= mouse[1] <= 540:
					print("play")
					main("null")
				if 500 <= mouse[0] <= 700 and 550 <= mouse[1] <= 590:
					print("setting")
				if 500 <= mouse[0] <= 700 and 600 <= mouse[1] <= 640:
					print("exit")
					pygame.quit()
					sys.exit()
 
	mouse = pygame.mouse.get_pos()
	buttons_draw()
 
	pygame.display.update() 
	clock.tick(60)