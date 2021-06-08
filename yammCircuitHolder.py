#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import scriptYourPanel

FNAME = os.path.basename(os.path.splitext(sys.argv[0])[0])

IMG_PATH = "img"
filename = "%s/%s.svg"%(IMG_PATH, FNAME)
sketch = scriptYourPanel.SKETCH(filename, "mm")

# I don't know why drawing is out of the sheet, but I can fix it
x_origin = 129.0
y_origin = -157.0
sketch.changeOrigin(x_origin, y_origin)

HOLE_RADIUS = 1.6
LCD_4x20_WIDTH = 97.2
LCD_4x20_HEIGHT = 40.0
LDC_4x20_HOLE_X_INTERVAL = 93.0
LDC_4x20_HOLE_Y_INTERVAL = 55.0
LCD_4x20_CONNECTOR_WIDTH = 40.65
LCD_4x20_CONNECTOR_HEIGHT = 2.54 * 1.5
LCD_SCREEN_WIDTH = 76.22
LCD_SCREEN_HEIGHT = 25.41

# display 4 lines of 20 characters
#~ sketch.addComponent("lcd4x20", 0.0, 0.0)

sketch.addRectangle(-5.5, 0.0, 109.0, 60.0)

sketch.addCircle(- LDC_4x20_HOLE_X_INTERVAL / 2, - LDC_4x20_HOLE_Y_INTERVAL / 2, HOLE_RADIUS)
sketch.addCircle(+ LDC_4x20_HOLE_X_INTERVAL / 2, - LDC_4x20_HOLE_Y_INTERVAL / 2, HOLE_RADIUS)
sketch.addCircle(- LDC_4x20_HOLE_X_INTERVAL / 2, + LDC_4x20_HOLE_Y_INTERVAL / 2, HOLE_RADIUS)
sketch.addCircle(+ LDC_4x20_HOLE_X_INTERVAL / 2, + LDC_4x20_HOLE_Y_INTERVAL / 2, HOLE_RADIUS)

sketch.addText("Yamm Pocket's circuit holder", 0.0, 0.0, anchor = "middle", font_size = 1.0)
sketch.addText("TOP", 0.0, 25.0, anchor = "middle", font_size = 1.0)
sketch.addText("BOTTOM", 0.0, - 25.0, anchor = "middle", font_size = 1.0)

sketch.addComponent("yammHolesV1", -5.5, 0.0)

sketch.save()

