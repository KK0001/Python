# -*- coding: utf-8 -*-
import math

print("0から90度までのsin,cos,tanを表示します！")

for i in range(0,90):
    z1 = math.pi/180 * i
    print(math.sin(z1), math.cos(z1), math.tan(z1))

z2=math.pi/2
print(math.sin(z2), math.cos(z2))
print("90度ではtanは定義できないの！")
print(math.cos(math.pi/2))

#コサインの90度がよくわからない表示になってしまう。僕はcos0はoだと思っていたのだが。