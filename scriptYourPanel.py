#!/usr/bin/python
# -*- coding: utf-8 -*-

# 
# file : scriptSvg.py
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

#~ if sys.version_info[0] < 3:
    #~ # python 2 or less
    #~ import Tkinter as gui
    #~ import tkMessageBox as gui_mb
    #~ import tkSimpleDialog as gui_sd
    #~ import tkFileDialog as gui_fd
    #~ import tkFont as gui_font
    #~ USING_PYTHON2 = True
#~ else:
    #~ # python 3 or more
    #~ import tkinter as gui
    #~ from tkinter import messagebox as gui_mb
    #~ from tkinter import simpledialog as gui_sd
    #~ from tkinter import filedialog as gui_fd
    #~ from tkinter import font as gui_font
    #~ USING_PYTHON2 = False

sys.stdout.write(sys.version + "\n")
sys.stdout.write("scriptYourPanel v. 1.00\n")

TEMPLATE = "template"
RECTANGLE = "rectangle"
LINE = "line"
TEXT = "text"
ELLIPSE = "ellipse"

#~ COEFF = 1.0

# text--align : start middle end

class SKETCH():
    RECTANGLE_ID = 1
    LINE_ID = 1
    ELLIPSE_ID = 1
    TEXT_ID = 1
    
    def __init__(self, fname, unit="mm"):
        self.changeUnit(unit)
        self.__x_origin = 0.0
        self.__y_origin = 0.0
        self.__fname = fname
        self.__objects = {}
        self.__raw_xy = {}
        
        #~ self.__drawSkecth = False
        #~ self.__win = gui.Tk()
        #~ self.__canvas = gui.Canvas(self.__win)
        #~ self.__canvas.grid()
        #~ self.__drawSkecth = True
        
 #~ def getWin(self):
        #~ return self.__win
        
    def __getBinObject(self, fname):
        return open("bin/" + fname + ".bin", "r").read(-1)
        
    def cvrt(self, value):
        return float(value) * self.__coeff

    def changeUnit(self, unit):
        if unit ==  "mm":
            self.__coeff = 1.0
        elif unit == "cm":
            self.__coeff = 10.0
        elif unit == "in":
            self.__coeff = 25.4
        else:
            raise Exception("Not implemented unit \"%s\"\n"%self.__unit)
        self.__unit = unit

    def changeOrigin(self, x, y):
        self.__x_origin = self.cvrt(x)
        self.__y_origin = -self.cvrt(y)
    
    def translation(self, x, y):
        x += self.__x_origin
        y += self.__y_origin
        return x, y

    def addRectangle(self, x, y, w, h, radius=0, label=None):
        key = "rect%u"%SKETCH.RECTANGLE_ID
        SKETCH.RECTANGLE_ID += 1
        if label == None:
            label = key
        self.__raw_xy[label] = float(x), float(y)
        x, y, w, h, radius = self.cvrt(x), self.cvrt(y), self.cvrt(w), self.cvrt(h), self.cvrt(radius)
        x = x - w / 2.0 
        y = 0.0 - y - h / 2.0 
        x += self.__x_origin
        y += self.__y_origin
        self.__objects[key] = [x, y, w, h, radius]
        
        #~ self.__canvas.create_rectangle(x * COEFF, y * COEFF, w * COEFF, h * COEFF, outline="black")

        return key

    def addLine(self, x1, y1, x2, y2, label=None):
        key = "line%u"%SKETCH.LINE_ID
        SKETCH.LINE_ID += 1
        if label == None:
            label = key
        self.__raw_xy[label] = float(x1), float(y1)
        x1, y1, x2, y2 = self.cvrt(x1), self.cvrt(y1), self.cvrt(x2), self.cvrt(y2)
        x1 += self.__x_origin
        y1 += self.__y_origin
        x2 += self.__x_origin
        y2 += self.__y_origin - y2
        self.__objects[key] = [x1, y1, x2-x1, y2-y1]
        return key

    def addCircle(self, x, y, r, label=None):
        key = "elli%u"%SKETCH.ELLIPSE_ID
        SKETCH.ELLIPSE_ID += 1
        if label == None:
            label = key
        self.__raw_xy[label] = float(x), float(y)
        x, y, r = self.cvrt(x), 0.0 - self.cvrt(y), self.cvrt(r)
        x += self.__x_origin
        y += self.__y_origin
        self.__objects[key] = [x, y, r]
        return key

    def addText(self, text, x, y, font_size=1.5, anchor="start", transform=None, label=None):
        font_size = self.cvrt(font_size)
        key = "text%u"%SKETCH.TEXT_ID
        SKETCH.TEXT_ID += 1
        if label == None:
            label = key
        self.__raw_xy[label] = float(x), float(y)
        x, y = self.cvrt(x), self.cvrt(y)
        y = 0.0 - y
        x += self.__x_origin
        y += self.__y_origin
        self.__objects[key] = [x, y, str(text), font_size, anchor, transform]
        return key

    def addComponent(self, object_name, x, y):
        code = open("lib/%s.syp"%object_name).read(-1)
        exec(code)
        function_name = "add" + object_name[0].upper() + object_name[1:] 
        exec("%s(self, %f, %f)"%(function_name, x, y))

    def save(self):
        objects_code = ""
        for key in self.__objects.keys():
            object = self.__objects[key]
            if key.startswith("rect"):
                code = self.__getBinObject(RECTANGLE)
                code = code.replace("#ID#", key)
                code = code.replace("#X#", str(object[0]))
                code = code.replace("#Y#", str(object[1]))
                code = code.replace("#W#", str(object[2]))
                code = code.replace("#H#", str(object[3]))
                code = code.replace("#RX#", str(object[4]))
                code = code.replace("#RY#", str(object[4]))
                objects_code += code
            elif key.startswith("line"):
                code = self.__getBinObject(LINE)
                code = code.replace("#ID#", key)
                code = code.replace("#X#", str(object[0]))
                code = code.replace("#Y#", str(object[1]))
                code = code.replace("#W#", str(object[2]))
                code = code.replace("#H#", str(object[3]))
                objects_code += code
            elif key.startswith("elli"):
                code = self.__getBinObject(ELLIPSE)
                code = code.replace("#ID#", key)
                code = code.replace("#X#", str(object[0]))
                code = code.replace("#Y#", str(object[1]))
                code = code.replace("#RX#", str(object[2]))
                code = code.replace("#RY#", str(object[2]))
                objects_code += code
            elif key.startswith("text"):
                code = self.__getBinObject(TEXT)
                if object[5] == None:
                    code = code.replace("#TRANSFORM#", "")
                else:
                    code = code.replace("#TRANSFORM#", 'transform="rotate(%s)"'%object[5])
                    if object[5] == "-90":
                        temp = object[0]
                        object[0] = -object[1]
                        object[1] = temp
                    if object[5] == "180":
                        object[0] = -object[0]
                        object[1] = -object[1]
                        # TODO: implement 90 & 180
                code = code.replace("#ID#", key)
                code = code.replace("#X#", str(object[0]))
                code = code.replace("#Y#", str(object[1]))
                code = code.replace("#TEXT#", str(object[2]))
                code = code.replace("#FONT_SIZE#", str(object[3]))
                code = code.replace("#TEXT_ANCHOR#", str(object[4]))
                objects_code += code
        full_code = self.__getBinObject(TEMPLATE)
        full_code = full_code.replace("#DOC_NAME#", self.__fname)
        full_code = full_code.replace("#OBJECTS#", objects_code)
        with open(self.__fname, "w") as fp:
            fp.write(full_code)
        sys.stdout.write("file %s saved.\n"%self.__fname)

if __name__ == "__main__":

    print(sys.argv)

    sketch = SKETCH('img/test.svg', "in")

    # I don't know why drawing it out of the sheet, but I can fix it
    sketch.changeOrigin(6, -7.5)

    # let's compute front pannel border
    sketch.addRectangle(0, 0, 7.8, 5.2, 0.15)

    y = 1.0
    for x in (1.0, 2.0, 3.0, 4.0) :
        sketch.addLine(x, y, x+0.8, y+0.2)
    
    sketch.save()
    