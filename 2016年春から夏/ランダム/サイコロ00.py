# -*- coding: utf-8 -*-

import random               #randomをimport

def dice():                 #1~6の数字をランダムに返す関数
    return random.randint(1, 6)

print(dice())               #実効値を表示

"""
http://qiita.com/mia_0032/items/9547c1c2c154fce1605a
を参照

↑を動かす時はこう。

# -*- coding: utf-8 -*-

import random

class Dice(object):
    def throw(self):
        return random.randint(1, 6)

n=Dice()
print(n.throw())

"""