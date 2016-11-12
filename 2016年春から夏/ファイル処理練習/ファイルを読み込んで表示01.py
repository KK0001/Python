# -*- coding: utf-8 -*-

f=open("foo2.txt","r",encoding="utf-8")#ファイルを読み込む
for line in f:#一行ずつ文字列をファイルから読み込む
    print(line,end="")#出力
