from turtle import *

shape('turtle')
color('red')

for diamond in range(4):
    for line in range(8):
        if line == 0:
            right(30)
        elif line == 2 or line == 6:
            left(60)
        elif line == 4:
            left(120)
        else:
            forward(100)
    right(120)

mainloop()