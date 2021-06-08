#!/usr/bin/python
# -*- coding: utf-8 -*-

# 
# file : test.py
# Copyright (c) pfeuh <ze.pfeuh@gmail>
# All rights reserved.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 

import sys
import os
import scriptYourPanel

FNAME = os.path.basename(os.path.splitext(sys.argv[0])[0])

IMG_PATH = "img"
filename = "%s/%s.svg"%(IMG_PATH, FNAME)
sketch = scriptYourPanel.SKETCH(filename, "mm")

# I don't know why drawing it out of the sheet, but I can fix it
sketch.changeOrigin(152.0, -190.0)

WIDTH = 452.0
HEIGHT = 44.0

HOLE_RADIUS = 10.7 /2.0
HOLES_H_WIDTH = 415.0
NB_HOLES = 24.0
HOLES_NB_INTERVALS = NB_HOLES - 1.0
HOLE_STEP = HOLES_H_WIDTH / HOLES_NB_INTERVALS
x = -HOLES_H_WIDTH / 2.0
y = 20.6 / 2.0

LABELS = [
    ["MOJO", "middleRight", "[L"],
    ["", "middle", "R]"],
    ["MLOG", "middle", "OUT"],
    ["P800", "middle", "OUT"],
    ["", "left", "[HI"],
    ["LAMBDA", "middleRight", "LO"],
    ["", "middle", "MIX"],
    ["", "middle", "SUST]"],
    ["", "middle", "9"],
    ["", "middle", "10"],
    ["", "middle", "11"],
    ["", "middle", "12"],
    ["", "middle", "13"],
    ["", "middle", "14"],
    ["", "middle", "15"],
    ["", "middle", "16"],
    ["", "middle", "17"],
    ["", "middle", "18"],
    ["", "middle", "19"],
    ["MS20", "middle", "OUT"],
    ["SLIM", "middle", "OUT"],
    ["M500", "middle", "OUT"],
    ["MOD", "middle", "OUT"],
    ["BOOG", "middle", "OUT"],
    ]

sketch.addRectangle(0.0, 0.0, WIDTH, HEIGHT, 0.0)

for column_num in range(len(LABELS)):
    sketch.addCircle(x, y, HOLE_RADIUS)
    sketch.addCircle(x, -y, HOLE_RADIUS)
    x_text = x
    x_text2 = x_text
    anchor = LABELS[column_num][1]
    if anchor == "middleRight":
        anchor = "middle"
        x_text2 += HOLE_STEP / 2.0
    sketch.addText(LABELS[column_num][0], x_text2, -2.0 + HOLE_STEP, anchor=anchor)
    anchor = "middle"
    sketch.addText(LABELS[column_num][2], x_text, -2.0, anchor=anchor)
    x += HOLE_STEP

sketch.save()




