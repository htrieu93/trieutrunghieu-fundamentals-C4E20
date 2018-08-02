from turtle import *

i = 52

shape('turtle')
color('yellow')
pen({'pencolor' : 'blue'})
speed(-1)
   
while i > 0:
    circle(100)
    right(7)
    i -= 1

mainloop()