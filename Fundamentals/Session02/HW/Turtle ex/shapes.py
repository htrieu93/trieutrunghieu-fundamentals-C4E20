from turtle import *

shape('turtle')

for shape in range(3,7):
    forward(100)
    if (shape % 2) == 1:
        color('blue')
    else:
        color('red')
    for i in range(shape - 1):
        left(360 / shape)
        forward(100)
    left(360 / shape)
        
mainloop()