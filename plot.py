from mandelbrot import mandelbrot,max_iter
from PIL import Image, ImageDraw
'''for reference 
https://www.codingame.com/playgrounds/2358/how-to-plot-the-mandelbrot-set/adding-some-colors
'''
#IMAGE size 
width = 600
height = 400 
#plot window 
re_start = -2
re_end = 1
im_start = -1 
im_end = 1

palette= []

#im = Image.new('RGB',(width,height),(0,0,0))
im = Image.new('HSV',(width,height),(0,0,0))
draw = ImageDraw.Draw(im)

for x in range(0,width):
    for y in range(0,height):
        #convert pixel coordinates to complex number 
        c = complex(re_start + (x/width)*(re_end-re_start),im_start + (y/height)*(im_end-im_start))
        #computing the number of iterations 
        m = mandelbrot(c)#will give the number of iterations after which either the complex number blows up or reaches the maximum iterations,i.e 80
        '''#the color depends on the number of iterations 
        color = 255 - int(m*255/max_iter)
        #ploting the point '''
        #the color depends on the number of iterations 
        hue = int(255*m/max_iter)
        saturation = 255
        value = 255 if m < max_iter else 0
        #plotting the point
        #draw.point([x,y],(color,color,color))
        draw.point([x,y],(hue,saturation,value))

im.convert('RGB').save('output.png','PNG')       