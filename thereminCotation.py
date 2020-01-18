#!/usr/bin/python
# -*- coding: utf-8 -*-

WIDTH = 660.0
NB_KEYS = float(49)
KEY_WIDTH = WIDTH/NB_KEYS
HEIGHT = 20.0
HOLE_RADIUS = 1.5

import sys
import os
import scriptYourPanel

FNAME = os.path.basename(os.path.splitext(sys.argv[0])[0])

IMG_PATH = "img"
filename = "%s/%s.svg"%(IMG_PATH, FNAME)
sketch = scriptYourPanel.SKETCH(filename, "mm")

# I don't know why drawing it out of the sheet, but I can fix it
sketch.changeOrigin(152.0, -190.0)

sketch.addRectangle(0.0, 0.0, WIDTH, HEIGHT)

for x1 in range(int(NB_KEYS)):
    x = (float(x1 + 0.5) * KEY_WIDTH) - (WIDTH / 2.0)
    sketch.addCircle(x, 0.0, HOLE_RADIUS)

    




sketch.save()

