scriptYourPanel is a brutal hack of .svg files

Generated objects:
- rectangles (to cut)
- circles (to cut)
- text (to engrave)
- scripteds objects

Have a look at a scripted object in "lib" directory, it's pretty simple

text are able to:
- use 4 directions, up, down, left and right
- use 3 anchors, start, middle and end

The target is to create files for lasercut machine.

As it is extreme programming, I've only implemented what I need.

How does it work? I sliced a dummy svg file (which is an XML file)
with a circle, a text and a rectangle objects. I use theses sliced
texts as templates, filling coordinates and other cool stuff directly
in scripting or using library objects.

The main problem for me was to create texts in 4 directions with
the 3 anchors start, middle & end. It's now fixed.

