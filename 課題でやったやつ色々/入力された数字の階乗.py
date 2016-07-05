# -*- coding: utf-8 -*-

a = input("入力した自然数の階乗を求めるよ！\n==>")
x=1

if int(a)>0:
    print("計算します！")
    for i in range(1,int(a)+1):
        x *= i
    print("階乗は",int(x),"です！")


elif int(a)<=0:
    print("自然数を入力してって言ったじゃん！")



