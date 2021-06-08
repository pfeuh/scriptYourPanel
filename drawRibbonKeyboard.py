#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO: bug if transpose != 0

import sys
import os
import scriptYourPanelAbsolute

DEBUG = "-d" in sys.argv

def drawLine(sketch, note_name, x1, y1, x2, y2):
    if DEBUG:
        sys.stdout.write("%-02s line      %6.2f %6.2f %6.2f %6.2f\n"%(note_name, x1, y1, x2, y2) )
    sketch.addLine(x1, y1, x2, y2)

def drawRectangle(sketch, note_name, x1, y1, x2, y2):
    if DEBUG:
        sys.stdout.write("%-02s rectangle %6.2f %6.2f %6.2f %6.2f\n"%(note_name, x1, y1, x2, y2) )
    sketch.addRectangle(x1, y1, x2, y2)

def drawCircle(sketch, note_name,x, y, r):
    if DEBUG:
        sys.stdout.write("%-02s circle    %6.2f %6.2f %6.2f\n"%(note_name, x, y, r))
    sketch.addCircle(x, y, r)
    
def drawKeyboard(nb_notes, transpose, keyboard_width, white_height,
                 black_height, no_black=False, no_hole=True, hole_radius=3.0):
    FNAME = os.path.basename(os.path.splitext(sys.argv[0])[0])
    IMG_PATH = "img"
    filename = "%s/%s.svg"%(IMG_PATH, FNAME)
    sketch = scriptYourPanelAbsolute.SKETCH(filename, "mm")

    # don't change this
    WHITE = True
    BLACK = not WHITE
    NOTE_NAME =      ["C",   "C#", "D",   "D#", "E",   "F",   "F#", "G",   "G#", "A",   "A#", "B"]
    NOTE_TYPE =      [WHITE, BLACK,WHITE, BLACK,WHITE, WHITE, BLACK,WHITE, BLACK,WHITE, BLACK,WHITE]
    NB_NOTE_PER_STAVE = 12
    BLACK_WIDTH = keyboard_width / float(nb_notes)
    SMALL_WIDTH = BLACK_WIDTH * 5.0 / 3.0
    BIG_WIDTH = BLACK_WIDTH * 7.0 / 4.0

    if NOTE_TYPE[transpose] == BLACK:
        raise Exception("Not able to left starting with a black key!")

    if DEBUG:
        sys.stdout.write("nb_notes       %3u\n"%nb_notes)
        sys.stdout.write("transpose      %3u\n"%transpose)
        sys.stdout.write("keyboard_width %6.2f\n"%keyboard_width)
        sys.stdout.write("BLACK_WIDTH    %6.2f\n"%BLACK_WIDTH)
        sys.stdout.write("SMALL_WIDTH    %6.2f\n"%SMALL_WIDTH)
        sys.stdout.write("BIG_WIDTH      %6.2f\n"%BIG_WIDTH)
        sys.stdout.write("white_height   %6.2f\n"%white_height)
        sys.stdout.write("black_height   %6.2f\n"%black_height)

    # drawing keyboard outline
    sketch.addRectangle(0.0, 0.0, keyboard_width, white_height)

    white_pos = 0.0

    for note_index in range(nb_notes):
        idx = (note_index + transpose)
        x1 = float(note_index) * BLACK_WIDTH
        y1 = 0.0
        note_name = NOTE_NAME[idx % NB_NOTE_PER_STAVE]

        if NOTE_TYPE[idx % NB_NOTE_PER_STAVE] == WHITE:
            #drawing white notes
            if note_name in ("C",):
                # C and F are specials, they are preceded by another white key
                drawLine(sketch, note_name, white_pos, y1, white_pos, white_height)
                white_pos += SMALL_WIDTH

            elif note_name in ("D", "E"):
                # C and F are specials, they are preceded by another white key
                drawLine(sketch, note_name,white_pos, y1, white_pos, white_height - black_height)
                white_pos += SMALL_WIDTH

            elif note_name in ("F",):
                # C and F are specials, they are preceded by another white key
                drawLine(sketch, note_name, white_pos, y1, white_pos, white_height)
                white_pos += BIG_WIDTH

            elif note_name in ("G", "A", "B", "B"):
                # C and F are specials, they are preceded by another white key
                drawLine(sketch, note_name,white_pos, y1, white_pos, white_height - black_height)
                white_pos += BIG_WIDTH
                
        else:
            # drawing black notes
            if not no_black:
                drawRectangle(sketch, note_name, x1, white_height - black_height, BLACK_WIDTH, black_height)
            if not no_hole:
                x_hole = x1  + 0.5 * BLACK_WIDTH
                drawCircle(sketch, note_name, x_hole, - white_height + black_height / 3.0, hole_radius)
                drawCircle(sketch, note_name, x_hole, - white_height + black_height / 3.0 * 2.0, hole_radius)

    sketch.save()
    
if __name__ == "__main__":

    # user configuration - dimensions in millimeters
    NB_NOTES = 37
    TRANSPOSE = 0
    KEYBOARD_WIDTH = 481.0
    WHITE_HEIGHT = 90.0
    BLACK_HEIGHT = 60.0

    drawKeyboard(NB_NOTES,
                 TRANSPOSE,
                 KEYBOARD_WIDTH,
                 WHITE_HEIGHT,
                 BLACK_HEIGHT,
                 no_black=True,
                 no_hole=False,
                 hole_radius=1.5)