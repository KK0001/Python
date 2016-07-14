# -*- coding: utf-8 -*-

import random

class Dice(object):
    def throw(self):
        return random.randint(1, 6)

n=Dice()
print(n.throw())

"""
サイコロ
http://qiita.com/mia_0032/items/9547c1c2c154fce1605a
のものを引用
"""