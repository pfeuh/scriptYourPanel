#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os
import scriptYourPanel

WHITE = True
BLACK = not WHITE
NOTES = [WHITE, BLACK,WHITE, BLACK,WHITE, WHITE, BLACK,WHITE, BLACK,WHITE, BLACK,WHITE] * 2 + [WHITE]
# Yamaha's Genos keyboard data
NB_STAVES = 6.0
NB_WHITE_PER_STAVE = 7.0
NB_BLACK_PER_STAVE = 5.0
WIDTH_FOR_1_STAVE = 985.5 / NB_STAVES
WHITE_WIDTH = WIDTH_FOR_1_STAVE / NB_WHITE_PER_STAVE
BLACK_WIDTH = WIDTH_FOR_1_STAVE / (NB_WHITE_PER_STAVE + NB_BLACK_PER_STAVE)
WHITE_HEIGHT = 140
BLACK_HEIGHT = 90

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

