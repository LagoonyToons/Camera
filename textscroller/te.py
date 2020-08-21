import pygame as pg
import random
import sys
from textscrollnl import *


pg.init()

width = 1080
height = 720
display = pg.display.set_mode((width, height))

pg.display.set_caption('Text scroll Test')
offset = 50

string1 = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast is ready! Ooming! Hang on a second. Hello? - Barry? - Adam? - Oan you believe this is happening? - I can't. I'll pick you up. Looking sharp. Use the stairs. Your father paid good money for those. Sorry. I'm excited. Here's the graduate. We're very proud of you, son. A perfect report card, all B's. Very proud. Ma! I got a thing going here. - You got lint on your fuzz. - Ow! That's me! - Wave to us! We'll be in row 118,000. - Bye! Barry, I told you, stop flying in the house! - Hey, Adam. - Hey, Barry."
while True: # main game loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                text = DynamicText(string1, (offset, height/12), delay=4, offset = 20, color=pg.Color("red"))
    pg.display.update()
    display.fill(pg.Color('black'))
    #pg.display.update()
    try:
        text.update()
        text.draw(display)
    except:
        pass
