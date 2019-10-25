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

#~ sketch.addComponent("keyboard4x4", 0, 0)
#~ sketch.addComponent("lcd4x20", 100, 0)
#~ sketch.addComponent("encoder", 0, 50)
#~ sketch.addComponent("centrakorPanel", 0, 0)
#~ sketch.addComponent("tekoPanel", 0, 0)
#~ sketch.addComponent("yassPanel", 0, 0)
#~ sketch.addComponent("onOffPanelPlug", -100, 0)
#~ sketch.addComponent("powerPanelPlug", -100, 30)
#~ for x in range(3):
    #~ sketch.addComponent("din5", x * 30 + 25, 50)
#~ sketch.addComponent("verticalJoystick", -140, 0)
#~ sketch.addComponent("horizontalJoystick", -100, 100)
#~ for x in range(8):
    #~ sketch.addComponent("miniJackPanel", -70 + x * 10, -50)
#~ sketch.addComponent("interrupteurBascule", -50, 0)

sketch.addComponent("tekoPanel", 0, 0)
sketch.addComponent("centrakorPanel", 0, 0)
sketch.addComponent("yassPanel", 0, 0)
sketch.addComponent("yassStuff", 0, 0)

sketch.save()

