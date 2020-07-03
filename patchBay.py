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
    ["L", "D3200"], # 0
    ["R", ""], # 1
    ["L", "ZOOM R16"], # 2
    ["R", "" ], # 3
    ["L", "COMPUTER"], # 4
    ["R", ""], # 5
    ["OUT", "MS-20"], # 6
    ["OUT", "MLOG"], # 7
    ["OUT", "LAMB"], # 8
    ["L", "GENOS-IN"], # 9
    ["R", ""], # 10
    ["L", "GENOS-OUT"], # 11
    ["R", ""] ,# 12
    ["1", ""], # 13
    ["2", "----- GENOS AUX ----"], # 14
    ["3", ""], # 15
    ["4", ""], # 16
    ["L", ""], # 17
    ["R", ""], # 18
    ["1", "------------------- MPC -------------------"], # 19
    ["2", ""], # 20
    ["3",""], # 21
    ["4", ""], # 22
    ["", ""], # 23
    ]

sketch.addRectangle(0.0, 0.0, WIDTH, HEIGHT, 0.0)

for column_num in range(int(NB_HOLES)):
    sketch.addCircle(x, y, HOLE_RADIUS)
    sketch.addCircle(x, -y, HOLE_RADIUS)
    x_text = x
    sketch.addText(LABELS[column_num][0], x_text, -2.0 + HOLE_STEP, anchor = "middle")
    #~ x_text = x
    anchor = "middle"
    
    # let's customize a bit
    if column_num in(0, 2, 4, 9, 11, 14, 19):
        # text is center between the hole and the next hole
        x_text += 0.5 * HOLE_STEP
    #~ if column_num in(0,8, 12):
        #~ anchor = "start"
    #~ elif column_num in(7,11, 14):
        #~ anchor = "end"
        
    sketch.addText(LABELS[column_num][1], x_text, -2.0, anchor = anchor)

    x += HOLE_STEP

sketch.save()
#~ sketch.getWin().mainloop()




