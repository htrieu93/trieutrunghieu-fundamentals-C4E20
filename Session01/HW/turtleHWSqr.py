from turtle import *

i = 4

shape('turtle')
color('yellow')
pen({'pencolor' : 'blue'})
speed(-1)

begin_fill()
while i > 0:
    forward(100)
    left(90)
    i -= 1
end_fill()

mainloop()