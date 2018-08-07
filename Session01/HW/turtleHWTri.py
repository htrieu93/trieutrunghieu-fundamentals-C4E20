from turtle import *

i = 3

shape('turtle')
color('yellow')
pen({'pencolor' : 'blue'})
speed(-1)

begin_fill()
while i > 0:
    forward(100)
    left(120)
    i -= 1
end_fill()

mainloop()