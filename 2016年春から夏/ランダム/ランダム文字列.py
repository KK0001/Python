# -*- coding: utf-8 -*-

#入力した文字列をランダムに入れ替えて返す関数
def  get_random():
    import random                           #randomをimport
    str=input("文字列を入力してください→ ")     #文字列の入力
    random_str = ''                         #最終的に返す値
    for i in range(len(str)):               #ここのfor文で入れ替え
        random_str += random.choice(str)
    return random_str                       #結果を返す

print(get_random())#実際に実行して、返された値をprint


"""
http://atasatamatara.hatenablog.jp/entry/20110225/1298602964
を参照
"""