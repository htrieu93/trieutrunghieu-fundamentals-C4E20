from turtle import *

shape('turtle')
color('blue')
speed(-1)
square = 0
size = 150
right(45)

while square <50:
    square += 1
    for line in range(4):
        right(90)
        forward(size)
        
    right(10)
    size -= 3
    
mainloop()