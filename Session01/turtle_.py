from turtle import *

speed(-1)
shape('turtle')

color('red')

i = 12

# while i > 0:
#     forward(100)
#     left(90)
#     i -= 1
#     if i % 4 == 0:
#         right(60)

# for square in range(3):
#     for line in range(4):
#         forward(100)
#         left(90)
#     right(60)

n = int(input('Please enter a number: '))
i = n

begin_fill()
while i > 0:
    forward(100)
    left(360/n)
    i -= 1
end_fill()

mainloop()

