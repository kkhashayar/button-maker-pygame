
import pygame 
from pygame import mixer
from pygame.locals import *



pygame.init()
mixer.init()
clock = pygame.time.Clock()

################# CONSTANTS
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Buttons by K.Nariman simplepycodes ")
FPS = 45

cursor_image = pygame.image.load("cursor.png").convert_alpha()
cursor_sound = mixer.Sound("menu_sound_effect.ogg")

pygame.mouse.set_visible(False)



font_menu = pygame.font.SysFont(None, 30)
def draw_text(text, font, color, surface, x,y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x,y)
    surface.blit(text_obj, text_rect)


def create_button(name, frame,x,y, w,h, color_name, color_frame, text, function_name):
	name = pygame.Rect(x,y, w,h)
	frame = pygame.Rect(x,y, w+7,h+7)
	pygame.draw.rect(screen, (pygame.color.Color(color_frame)), frame)
	pygame.draw.rect(screen, (pygame.color.Color(color_name)), name)
	draw_text(text, font_menu, pygame.color.Color(color_frame), screen, x+25, y+5)

	if name.collidepoint((cursor_x,cursor_y)):
		pygame.draw.rect(screen, (pygame.color.Color(color_name)), frame)
		pygame.draw.rect(screen, (pygame.color.Color(color_frame)), name)
		draw_text(text, font_menu, pygame.color.Color(color_name), screen, x+25, y+5)
	
		if click:
			cursor_sound.play()
			function_name()

def test_collide():
	print("now clicked")


running = True 

while running:
	cursor_x, cursor_y = pygame.mouse.get_pos()
	click = False 
	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 

		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				click = True 



		screen.fill(pygame.color.Color("gray"))

		bt_start = create_button("start", "start_frame", 100,100, 100,30, "black", "white", "Start",test_collide)

		bt_music = create_button("Music", "music_frame", 100,150, 100,30, "black", "white", "Music",test_collide)

		bt_player = create_button("Player", "Player_frame", 100,200, 130,30, "black", "white", "Player",test_collide)

		bt_another = create_button("another", "another_frame", 100,250, 130,30, "black", "white", "Another",test_collide) 


	

		screen.blit(cursor_image,(cursor_x,cursor_y))
		pygame.display.flip()
