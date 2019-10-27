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

sketch.addComponent("centrakorPanel", -14.5, 0.0)
sketch.addComponent("yassStuff2", 0.0, 0.0)

step = 27.94
x = -102.0
y = -45.085
for comp_num, component_name in enumerate(("din5vertical", "din5vertical", "powerPanelPlug", "onOffPanelPlug")):
    sketch.addComponent(component_name, x, y)
    text = ("MIDI OUT", "MIDI IN", "POWER", "ON / OFF")[comp_num]
    sketch.addText(text, x, y + 12.0, anchor = "middle")
    y += step


sketch.save()

