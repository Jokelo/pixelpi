from screenfactory import create_screen
from modules.text_scroller import TextScroller
import config
import time
import pygame
import string

screen = create_screen()

text="Hello wop!"

scroller = TextScroller(screen, text,"3x7_font_printable.bmp")
scroller.start()

while True:
	if config.virtual_hardware:
		pygame.time.wait(10)
		for event in pygame.event.get():
			pass
	else:
		time.sleep(0.01)
