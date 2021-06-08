#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import scriptYourPanelAbsolute

WHITE = True
BLACK = not WHITE
NOTE_TYPE = [WHITE, BLACK, WHITE, BLACK, WHITE, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE]
# Yamaha's Genos keyboard data
NB_STAVES = 6.0
NB_NOTE_PER_STAVE = 12
NB_WHITE_PER_STAVE = 7.0
NB_BLACK_PER_STAVE = 5.0
WIDTH_FOR_1_STAVE = 985.5 / NB_STAVES
WHITE_WIDTH = WIDTH_FOR_1_STAVE / NB_WHITE_PER_STAVE
BLACK_WIDTH = WIDTH_FOR_1_STAVE / (NB_WHITE_PER_STAVE + NB_BLACK_PER_STAVE)
WHITE_HEIGHT = 140.0
BLACK_HEIGHT = 90.0
WHITE_HEIGHT /= 2.0
BLACK_HEIGHT /= 2.0
WHITE_OFFSET = - BLACK_WIDTH / 7.0

if __name__ == "__main__":

    FNAME = os.path.basename(os.path.splitext(sys.argv[0])[0])

    IMG_PATH = "img"
    filename = "%s/%s.svg"%(IMG_PATH, FNAME)
    sketch = scriptYourPanelAbsolute.SKETCH(filename, "mm")

    # I don't know why drawing is out of the sheet, but I can fix it
    #~ sketch.changeOrigin(152.0, -190.0)

    NB_NOTES = 3 * NB_NOTE_PER_STAVE + 1

    # White notes had to be drawn first
    flt_index = 0.0
    for note_index in range(NB_NOTES):
        if NOTE_TYPE[note_index % NB_NOTE_PER_STAVE] == WHITE:
            x1 = flt_index * WHITE_WIDTH + WHITE_OFFSET
            flt_index += 1.0
            #~ x1 = x
            #~ x +=  WHITE_WIDTH
            x2 = x1
            y1 = 0.0
            y2 = WHITE_HEIGHT
            # Is there a black note on left?
            if NOTE_TYPE[(note_index - 1) % NB_NOTE_PER_STAVE] == WHITE:
                # no
                sketch.addLine(x1, y1, x1, y2)
            else:
                # yes
                sketch.addLine(x1, y1 + BLACK_HEIGHT, x1, y2)

    for note_index in range(NB_NOTES):
        flt_index = float(note_index)
        if NOTE_TYPE[note_index % 12] == BLACK:
            x1 = flt_index * BLACK_WIDTH
            x2 = x1 + BLACK_WIDTH
            y1 = 0.0
            y2 = BLACK_HEIGHT
            sketch.addRectangle(x1, y1, BLACK_WIDTH, BLACK_HEIGHT)

    # Adjusting right of last key
    sketch.addLine(0.0, 0.0, float(NB_NOTES) * BLACK_WIDTH, 0.0)
    sketch.addLine(0.0, WHITE_HEIGHT, float(NB_NOTES + 1) * BLACK_WIDTH, WHITE_HEIGHT)
    sketch.addLine(float(NB_NOTES) * BLACK_WIDTH, 0.0, float(NB_NOTES) * BLACK_WIDTH, BLACK_HEIGHT)
    sketch.addLine(float(NB_NOTES + 1) * BLACK_WIDTH, BLACK_HEIGHT, float(NB_NOTES + 1) * BLACK_WIDTH, WHITE_HEIGHT)
    sketch.addLine(float(NB_NOTES) * BLACK_WIDTH, BLACK_HEIGHT, float(NB_NOTES + 1) * BLACK_WIDTH, BLACK_HEIGHT)

sketch.save()

