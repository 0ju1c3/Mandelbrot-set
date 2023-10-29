#mandelbrot set 
#z = z * z + c
'''for reference 
https://www.codingame.com/playgrounds/2358/how-to-plot-the-mandelbrot-set/adding-some-colors
'''
from math import log, log2 

max_iter = 80
def mandelbrot(c):
    z = 0#complex number
    n = 0 #number of iterations it takes to blow up 
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n +=1 
    if n == max_iter:
        return max_iter 
    return n #+ 1 - log(log2(abs(z)))

if __name__ == "__main__":
    for a in range(-10,10,5):
        for b in range(-10,10,5):
            c = complex(a/10,b/10)
            print(c,mandelbrot(c))