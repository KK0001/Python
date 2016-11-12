# -*- coding: utf-8 -*-

#説明
print("入力された自然数2つの最大公約数を算出します。")

#入力部分
a = int(input("1つ目の自然数 → "))
b = int(input("2つ目の自然数 → "))

#b>aの時、中身を入れ替えます
if b>a:
    a,b=b,a

#ユークリッドのやつです
while a%b!=0:
    a,b=b,a%b

#出力部分
print("最大公約数は",b,"です。")

