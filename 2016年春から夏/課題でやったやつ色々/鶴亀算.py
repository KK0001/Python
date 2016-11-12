# -*- coding: utf-8 -*-

print("鶴亀算です。")

#入力部分
a=int(input("合計の足の数を入力してね=> "))
b=int(input("合計の頭の数を入力してね=> "))

#鶴亀算の一般化的なアレ
tsuru = a / 2 - b
kame = b - tsuru

if (tsuru<=0)|(kame<=0)|(a%2!=0):
    print("計算できません。")
else:
    print("鶴は",tsuru,"匹、亀は",kame,"匹だよ。")
