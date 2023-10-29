from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, max_iter
from collections import defaultdict
from math import floor, ceil
def linear_interpolation(color1, color2, t):#a line between two points, to get a good blend of colours
    return color1 * (1-t) + color2 * t

#image size 
width = 600 
height = 400 
re_start = -2
re_end = 1 
im_start = -1 
im_end = 1
 
histogram = defaultdict(lambda:0)
values = {}
for x in range(0,width):
    for y in range(0,height):
        #convert pixel coordinate to complex number 
        c = complex(re_start + (x/width) * (re_end-re_start),   im_start + (y/height)*(im_end-im_start))
        #compute the number of iterations
        m = mandelbrot(c)
        values[(x,y)] = m
        if m < max_iter:
            histogram[floor(m)] += 1
total = sum(histogram.values())
hues = []
h = 0
for i in range(max_iter):
    h += histogram[i]/total
    hues.append(h)
hues.append(h)
im = Image.new('HSV',(width,height),(0,0,0))
draw = ImageDraw.Draw(im)
for x in range(0,width):
    for y in range(0,height):
        m = values[(x,y)]
        #the color depends on the number of iterations 
        hue = 255 - int(255*linear_interpolation(hues[floor(m)],hues[ceil(m)],m%1))
        saturation = 255
        value = 255 if m < max_iter else 0
        #plotting the point 
        draw.point([x,y],(hue,saturation,value))
im.convert('RGB').save('mandelbrot-set_last.png','PNG')
