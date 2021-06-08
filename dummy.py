#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

WHITE = True
BLACK = not WHITE
NOTE_TYPE = [WHITE, BLACK,WHITE, BLACK,WHITE, WHITE, BLACK,WHITE, BLACK,WHITE, BLACK,WHITE]
ADJUSTEMENT = [False, False, False, False, True, False, False, False, False, False, False, True]
NOTE_NAME = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
NB_NOTE_PER_STAVE = 12

for x in range(13):
    idx = x % NB_NOTE_PER_STAVE
    text = "%-5s "%NOTE_NAME[idx]
    position = 1.0 / 12.0 * float(x)
    text += "%3.3f"%position
    
    if NOTE_TYPE[idx] == WHITE:
        if idx < 2:
            widx = WHITE_INDEX[idx]
            
    
    
    


    sys.stdout.write(text)
    sys.stdout.write("\n")
