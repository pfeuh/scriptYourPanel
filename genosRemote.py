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

sketch.addComponent("toyBox", 0, 0)
for jack_num in range(4):
    x = -52.5 + jack_num * 35.0
    y = 35.0
    sketch.addComponent("socketJack635", x, y)
    text = ["BLUE", "WHITE", "RED", "LESLIE"][jack_num]
    sketch.addText(text, x, y + 10.0, anchor="middle")

for obj_num in range(4):
    x = -52.5 + obj_num * 35.0
    y = -35.0
    component = ["socketJack635", "socketJack635", "din5", "powerPanelPlug"][obj_num]
    sketch.addComponent(component, x, y)
    text = ["SUSTAIN", "AUX", "MIDI OUT", "POWER"][obj_num]
    sketch.addText(text, x, y - 13.5, anchor="middle")

sketch.addComponent("arduinoNanoHolder", 45.0, 0.0)
sketch.addComponent("relayHolder", -45.0, 0.0)
sketch.addText("GENOS", 0.0, +10.0, anchor="middle", font_size=2.0)
sketch.addText("REMOTE", 0.0, -10.0, anchor="middle", font_size=2.0)



sketch.save()
