from turtle import *

n = 5
i = 0

shape('turtle')
color('blue')


# n = 0
# while n < 800:
#     forward(n)
#     left(90)
#     n += 5

# Alternate solutions:
    for n in (0, 800, 10):
        forward(n)
        left(90)
 
mainloop()