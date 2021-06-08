#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os
import scriptYourPanel

WHITE = True
BLACK = not WHITE
NOTES = [WHITE, BLACK,WHITE, BLACK,WHITE, WHITE, BLACK,WHITE, BLACK,WHITE, BLACK,WHITE] * 2 + [WHITE]
NOTE_WIDTH = 397 / 25.
WHITE_WIDTH = NOTE_WIDTH * 12.0 / 7.0
NOTE_HEIGHT = 40.0

FNAME = os.path.basename(os.path.splitext(sys.argv[0])[0])

IMG_PATH = "img"
filename = "%s/%s.svg"%(IMG_PATH, FNAME)
sketch = scriptYourPanel.SKETCH(filename, "mm")

# I don't know why drawing is out of the sheet, but I can fix it
#~ sketch.changeOrigin(152.0, -190.0)

white_x = NOTE_WIDTH / 3.0
for index in range(len(NOTES)):
    note = NOTES[index]
    x1 = float(index) * NOTE_WIDTH
    
    if note == WHITE:
        sketch.addRectangle(white_x, NOTE_HEIGHT / 2.0, WHITE_WIDTH, NOTE_HEIGHT * 2.0)
        white_x += WHITE_WIDTH
    else:
        sketch.addRectangle(x1, 0.0, NOTE_WIDTH, NOTE_HEIGHT)

sketch.save()

