# -*- coding: utf-8 -*-

def uranai(name):#nameに名前を入力、食べるべき料理が表示される。
    recipes=["麻婆胴部","オムライス","ハンバーグ","きゅうり"]
    print(name,"さんは")
    print(recipes[ord(name[0])%len(recipes)])#名前に応じてリストの中から一つ表示
    print("を食べると元気になれるよ！")

uranai("ボ")#例として「ボ」さんを占います



"""
recipes[ord(name[0])%len(recipes)]　の説明（自分用）
名前の1文字目をord()という関数を使って文字コードに変換。
その数値をリストの長さで割った余りをインデックスとして与え、リストの中から1つ項目を選んで出力。
"""