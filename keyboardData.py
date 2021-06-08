#!/usr/bin/python
# -*- coding: utf-8 -*-

NB_MIDI_NOTES = 128
NOTE_NAMES = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")

def getNoteName(note_num):
    stave_idx = x % 12
    stave = x /12 - 1
    return "%s%i"%(NOTE_NAMES[stave_idx],stave)


for x in range(128):
    print x, getNoteName(x)

