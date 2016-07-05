# -*- coding: utf-8 -*-

print("九九一覧を表示します。\n")

#計算部分
for i in range(1,10):
    for j in range(1,10):
        if i*j<10:
            print(" ", end="")
            print("",i*j, end="")
        else:
            print("",i*j, end="")
    print(" ")