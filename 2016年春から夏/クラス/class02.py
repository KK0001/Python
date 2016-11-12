# -*- coding: utf-8 -*-
import math

class Tp:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def content(self):
        return a*a*(math.pi)*b/3


print("三角錐の体積を計算します。")
a=int(input("底面の底辺 ==>"))
b=int(input("高さ ==>"))

p1=Tp(a,b)
print(p1.content())
