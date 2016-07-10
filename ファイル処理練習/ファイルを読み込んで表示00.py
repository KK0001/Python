# -*- coding: utf-8 -*-

f=open("foo.txt","r",encoding="utf-8")#ファイルをutf-8でエンコード（ファイルを開く）
s=f.read()#ファイルを文字列に変換
print(s)#sを表示
f.close()#ファイルを閉じる

#「はろー」と表示される