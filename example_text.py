from screenfactory import create_screen
from modules.text_scroller import TextScroller
import config
import time
import pygame
import string

screen = create_screen()

text="Hello World!"

scroller = TextScroller(screen, text,"3x7_font_printable.bmp")
scroller.start()
print("Displaying Text")
TextScroller.loop = 0

while TextScroller.loop!= 1:
	if config.virtual_hardware:
		pygame.time.wait(10)
		for event in pygame.event.get():
			pass
	else:
		time.sleep(0.01)
