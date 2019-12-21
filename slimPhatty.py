#!/usr/bin/python
# -*- coding: utf-8 -*-

# 
# file : slimPhatty.py
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

sys.stdout.write(sys.version + "\n")

import scriptYourPanel

HOLE_RADIUS = 1.6
HOLE_OFFSET = 6.0

FRONT_PANNEL_WIDTH = 133.0
FRONT_PANNEL_HEIGHT = 48.0

DRAW_FOOTPRINT = False

if __name__ == "__main__":

    FNAME = os.path.basename(os.path.splitext(sys.argv[0])[0])
    
    IMG_PATH = "img"
    filename = "%s/%s.svg"%(IMG_PATH, FNAME)
    sketch = scriptYourPanel.SKETCH(filename, "mm")
    
    # I don't know why drawing it out of the sheet, but I can fix it
    sketch.changeOrigin(152.0, -190.0)

    sketch.addLine(0.0, 0.0, FRONT_PANNEL_WIDTH, 0.0, label="L1")
    sketch.addLine(0.0, 0.0, 0.0, FRONT_PANNEL_HEIGHT, label="L2")
    sketch.addLine(FRONT_PANNEL_WIDTH, 0.0, FRONT_PANNEL_WIDTH, FRONT_PANNEL_HEIGHT, label="L3")
    
    sketch.save()
    #~ sketch.makeCSV("img/%s_coordinates.csv"%FNAME)

