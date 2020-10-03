#!/usr/bin/python
# -*- coding: utf-8 -*-

import scriptYourPanel as syp

sys = syp.sys

if __name__ == "__main__":

    sys.stdout.write(" ".join(sys.argv))

    sketch = syp.SKETCH('img/hideWindow.svg', "mm")

    # I don't know why drawing it out of the sheet, but I can fix it
    #~ sketch.changeOrigin(6, -7.5)

    # let's compute front pannel border
    sketch.addRectangle(0, 0, 978.0, 358.0, 0.15)

    #~ y = 1.0
    #~ for x in (1.0, 2.0, 3.0, 4.0) :
        #~ sketch.addLine(x, y, x+0.8, y+0.2)
    
    sketch.save()
    