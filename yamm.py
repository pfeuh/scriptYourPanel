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

NB_X_STEP = 4.0
width = 137.0
x_step = width / NB_X_STEP
NB_Y_STEP = 4.0
height = 135.0
y_step = height / NB_Y_STEP
y_text_offset = y_step / 2.7
y_big_bt_offset = 3.0
x_lcd_offset = 3.0
depth = 55
BUTTON_DIAMETER = 23.5
BUTTON_RADIUS = BUTTON_DIAMETER / 2.0
LED_WIDTH = 13.0
DIN5_WIDTH = 29.0
ENCODER_WIDTH = 18

def getXY(column, row):
    x = - width / 2.0 + x_step * column + x_step / 2
    y = - height / 2.0 + y_step * row + y_step / 2
    #~ print(column, row, x, y)
    return x, y

# the box
sketch.addComponent("centrakorQuasiSquareNoHole", 0, 0)

# right column: jack, interruptor, midi thru midi in
for comp_num, component_name in enumerate(("din5vertical", "din5vertical", "onOffPanelPlug", "powerPanelPlug")):
    x, y = getXY(3, comp_num)
    sketch.addComponent(component_name, x, y)
    text = ("IN", "THRU", "", "")[comp_num]
    sketch.addText(text, x, y + y_text_offset, anchor = "middle")

# CPU_RUN led
x, y = getXY(3, 2.5)
sketch.addComponent("led5mmHolder", x, y)

# beat per minute led
x, y = getXY(0, 1)
sketch.addComponent("led5mmHolder", x, y)
sketch.addText("Clock", x, y + y_text_offset, anchor = "middle")

# active sensing led
x, y = getXY(2, 1)
sketch.addText("Act.Sen.", x, y + y_text_offset, anchor = "middle")
sketch.addComponent("led5mmHolder", x, y)

# display 4 lines of 20 characters
x, y = getXY(1, 3)
sketch.addComponent("lcd4x20", x + x_lcd_offset, y - y_step / 2.0)

# encoder with switch button
x, y = getXY(1, 1)
sketch.addComponent("encoder", x, y)

# clear button
x, y = getXY(0, 0)
sketch.addText("Clear/Menu", x, y + y_text_offset + y_big_bt_offset, anchor = "middle")
sketch.addCircle(x, y, BUTTON_RADIUS)

# shift button
x, y = getXY(2, 0)
sketch.addText("Shift", x, y + y_text_offset + y_big_bt_offset, anchor = "middle")
sketch.addCircle(x, y, BUTTON_RADIUS)

# Name of the box
x, y = getXY(1, 3)
sketch.addText("YAMM", x + x_lcd_offset, y + 8.0, anchor = "middle", font_size = 2.0)

# subtitle
x, y = getXY(1, 2)
sketch.addText("Yet another MIDI monitor", x + x_lcd_offset, y - 8.0, anchor = "middle", font_size = 0.8)

# left and right sides
sketch.changeOrigin(x_origin - 100.0, y_origin)
for size_num, left_side_offset in enumerate((0.0, 200.0)):
    labels = ("UP - LEFT SIZE - DOWN", "UP - RIGHT SIZE - DOWN")
    sketch.addRectangle(left_side_offset, 0, 55.0, height)
    for y in range(int(NB_Y_STEP)):
        x, y = getXY(0, y)
        sketch.addRectangle(left_side_offset + depth / 4.0, y+1.5, depth / 2.0, 3.0)
    sketch.addRectangle(left_side_offset + depth / 4.0, height / 2.0 - 1.5, depth / 2.0, 3.0)
    sketch.addRectangle(left_side_offset + depth / 4.0, -height / 2.0 + 1.5, depth / 2.0, 3.0)
    sketch.addText(labels[size_num], x + left_side_offset + depth - 5.0, y - y_step * 1.5, anchor = "middle", font_size = 1.0)

# top & bottom sides
sketch.changeOrigin(x_origin - 58.0, y_origin - 158.0)

label_num = 0
for left_side_offset in (0.0, width + 3.0):
    labels = ("TOP SIDE BOTTOM", "BOTTOM SIDE BOTTOM")
    sketch.addRectangle(left_side_offset, 0, width, depth)
    sketch.addRectangle(left_side_offset + width / 2 - 1.5, depth / 4.0, 3.0, depth / 2.0)
    sketch.addRectangle(left_side_offset - width / 2 + 1.5, depth / 4.0, 3.0, depth / 2.0)
    sketch.addText(labels[label_num], x + left_side_offset + depth , y - y_step * 2.2, anchor = "middle", font_size = 1.0)
    label_num += 1

# reinforcement sides
#~ temp_offset = 58.0
temp_offset = 0.0
sketch.changeOrigin(x_origin - 58.0, y_origin - 100.0)
for index, left_side_offset in enumerate((0.0, width + 3.0)):
    labels = ("MIDI IN's LINE BOTTOM", "MIDI_THRU's LINE BOTTOM")
    item_widths = ((BUTTON_DIAMETER + 1.0, 0.0, BUTTON_DIAMETER + 1.0, DIN5_WIDTH), (LED_WIDTH, ENCODER_WIDTH, LED_WIDTH, DIN5_WIDTH, ))
    sketch.addRectangle(temp_offset + left_side_offset, 0, width, depth)
    sketch.addRectangle(temp_offset + left_side_offset + width / 2 - 1.5, depth / 4.0, 3.0, depth / 2.0)
    sketch.addRectangle(temp_offset + left_side_offset - width / 2 + 1.5, depth / 4.0, 3.0, depth / 2.0)
    sketch.addText(labels[index], temp_offset + left_side_offset, -depth * 0.4, anchor = "middle", font_size = 1.0)
    print(labels[index])
    for col, item_width in enumerate(item_widths[index]):
        x, y = getXY(col, y)
        if item_width != 0.0:
            sketch.addRectangle(x + temp_offset + left_side_offset, depth / 4.0, item_width, depth / 2.0)

sketch.save()

