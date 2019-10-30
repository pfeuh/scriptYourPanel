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

WIDTH = 440.0
HEIGHT = 44.0

sketch.addRectangle(0.0, 0.0, WIDTH, HEIGHT, 0.0)

HOLE_RADIUS = 9.7 /2.0
HOLES_WIDTH = 415.0
NB_HOLES = 24.0
HOLES_NB_INTERVALS = NB_HOLES - 1.0
HOLE_STEP = HOLES_WIDTH / HOLES_NB_INTERVALS
x = -HOLES_WIDTH / 2.0
y = HOLE_STEP / 2.0
LABELS_A = [
    "table", # 0
    "table", # 1
    "table", # 2
    "table", # 3
    "table", # 4
    "table", # 5
    "table", # 6
    "table", # 7
    "enr.", # 8
    "enr.", # 9
    "enr.", # 10
    "genos", # 11
    "genos", # 12
    "genos", # 13
    "genos", # 14
    "KING", # 15
    "", # 16
    "", # 17
    "", # 18
    "", # 19
    "", # 20
    "", # 21
    "", # 22
    "", # 23
    ]

LABELS_B = [
    "1", # 0
    "2", # 1
    "3", # 2
    "4", # 3
    "5/6", # 4
    "7/8", # 5
    "9/10", # 6
    "11/12", # 7
    "3/4", # 8
    "5/6", # 9
    "7/8", # 10
    "IN", # 11
    "MAIN", # 12
    "1/2", # 13
    "3/4", # 14
    "KORG", # 15
    "MS20", # 16
    "D", # 17
    "SLIM", # 18
    "", # 19
    "", # 20
    "", # 21
    "", # 22
    "", # 23
    ]

for hole_num in range(int(NB_HOLES)):
    sketch.addCircle(x, y, HOLE_RADIUS)
    sketch.addCircle(x, -y, HOLE_RADIUS)
    sketch.addText(LABELS_A[hole_num], x, -2.0 + HOLE_STEP, anchor = "middle")
    sketch.addText(LABELS_B[hole_num], x, -2.0, anchor = "middle")

    x += HOLE_STEP

sketch.save()
#~ sketch.getWin().mainloop()




