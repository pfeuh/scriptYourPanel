#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import scriptYourPanel

FNAME = os.path.basename(os.path.splitext(sys.argv[0])[0])

IMG_PATH = "img"
filename = "%s/%s.svg"%(IMG_PATH, FNAME)
sketch = scriptYourPanel.SKETCH(filename, "mm")

# I don't know why drawing it out of the sheet, but I can fix it
sketch.changeOrigin(152.0, -190.0)

sketch.addComponent("tekoPanel", 0, 0)
sketch.addComponent("yassStuff", 0, 0)

sketch.save()

