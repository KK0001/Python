# -*- coding: utf-8 -*-

print("入力された数が素数かを判別します。")

a=input("数=> ")#入力
b=0

#1は素数ではありません。
if a==1:
    print("素数ではありません。")

else:
    for i in range(2,int(a)):
        if b==0:#余りが無いとき
            print("素数です。")
        else:#余りがあるとき
            print("素数ではありません。")
