# -*- coding: utf-8 -*-

print("ネイピア数の算出を行うぞ！")

#変数の初期化的なアレです
x=1
n=1.0

#算出部分
for i in range(30):
    x *= i+1
    n +=1/x

#出力部分
print("ネイピア数は",n,"だぞ！")
