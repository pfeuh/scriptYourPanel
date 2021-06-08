#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
if sys.version_info[0] < 3:
    import Tkinter as gui
else:
    import tkinter as gui

WHITE = True
BLACK = not WHITE
NOTE_TYPE = [WHITE, BLACK,WHITE, BLACK,WHITE, WHITE, BLACK,WHITE, BLACK,WHITE, BLACK,WHITE]
NB_NOTE_PER_STAVE = 12
NB_STAVES = 6.0
NB_WHITE_PER_STAVE = 7.0
NB_BLACK_PER_STAVE = 5.0
WIDTH_FOR_1_STAVE = 580.0
WHITE_WIDTH = WIDTH_FOR_1_STAVE / float(NB_WHITE_PER_STAVE)
BLACK_WIDTH = WIDTH_FOR_1_STAVE / float(NB_NOTE_PER_STAVE)
FIRST_WHITE_WIDTH = BLACK_WIDTH * (5.0 / 3.0)
SECOND_WHITE_WIDTH = BLACK_WIDTH * (7.0 /4.0)
WHITE_HEIGHT = 400.0
BLACK_HEIGHT = 250.0
NB_NOTES = 3 * NB_NOTE_PER_STAVE + 1

def drawBlack(canvas, x1, y1, x2, y2, color="#000000", **kwds):
    if "fill" in kwds.keys():
        del(kwds["fill"])
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, **kwds)
    
def drawWhite(canvas, x1, y1, x2, y2, **kwds):
    kwds["fill"] = "#ffffff"
    kwds["outline"] = "#000000"
    canvas.create_polygon(x1, y1, x1, y2, x2, y2, x2, y1, **kwds)

if __name__ == "__main__":

    win = gui.Tk()
    win.title("Musical Keyboard")
    canvas = gui.Canvas(win, width=BLACK_WIDTH * (NB_NOTES + 1) + 10, height=WHITE_HEIGHT + 10, bg="green")
    canvas.grid()

    x = 0.0
    for note_index in range(NB_NOTES):
        flt_index = float(note_index)
        if NOTE_TYPE[note_index % NB_NOTE_PER_STAVE] == WHITE:
            x1 = x
            if (note_index % NB_NOTE_PER_STAVE) < 5:
                # width for C D E is stave / 12 * 5 / 3 
                x +=  FIRST_WHITE_WIDTH
            else:
                # width for F G A B is stave / 12 * 7 / 4 
                x +=  SECOND_WHITE_WIDTH
            x2 = x
            y1 = 0.0
            y2 = WHITE_HEIGHT
            drawWhite(canvas, x1, y1, x2, y2)

    for note_index in range(NB_NOTES):
        flt_index = float(note_index)
        if NOTE_TYPE[note_index % NB_NOTE_PER_STAVE] == BLACK:
            x1 = flt_index * BLACK_WIDTH
            x2 = x1 + BLACK_WIDTH
            y1 = 0.0
            y2 = BLACK_HEIGHT
            drawBlack(canvas, x1, y1, x2, y2, "#000000")

    win.mainloop()
