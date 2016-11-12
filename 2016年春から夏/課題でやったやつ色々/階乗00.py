# -*- coding: utf-8 -*-

print("入力された数の階乗を表示します。")


while 1:

    a=input("数=> ")
    x=1
    if int(a)>0:

        #計算部分
        for i in range(int(a)):
            x*=(i+1)
        print ('階乗は',x)
        continue

    elif int(a)==0:
        print ("階乗は",1)
        continue

    else:
        print("入力された数は負です！")
        break
