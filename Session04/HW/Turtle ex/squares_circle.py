from turtle import *

shape('turtle')
color('blue')
speed(-1)
square = 0

while square <24:
    square += 1
    for line in range(4):
        forward(100)
        left(90)
    left(15)
    
mainloop()