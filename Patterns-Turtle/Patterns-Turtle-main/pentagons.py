from turtle import *
import random

#setting the speed
speed(speed ='fastest')
  
def draw(n, x, angle):
    # loop for number of shape
    for i in range(n):
          
        colormode(255)
          
        # choosing random integers 
        # between 0 and 255
        # to generate random rgb values 
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
          
        # setting the outline 
        # and fill colour
        pencolor(a, b, c)
        fillcolor(a, b, c)
          
        # begins filling the shape
        begin_fill()
          
        # loop for drawing each shape
        for j in range(5):
            forward(5 * n-5 * i)
            right(x)
            
            
        # colour filling complete
        end_fill()
          
        # rotating for
        # the next shape
        right(angle)
          
  
# setting the parameters
n = 30    # number of stars
x = 72 # exterior angle of each shape
angle = 18    # angle of rotation for the spiral
  
draw(n, x, angle)
