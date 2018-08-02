from turtle import *

shape('turtle')
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for shape in range(3,8):
    color(colors[shape - 3 ])
    forward(100)
    for i in range(shape - 1):
        left(360 / shape)
        forward(100)
    left(360 / shape)
        
mainloop()