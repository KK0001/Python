from turtle import *

degree = 1
distance = 50
for i in range(40):
    forward(distance)
    right(degree)
    degree += 2
    distance -= 1

input()