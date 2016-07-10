# -*- coding: utf-8 -*-
from turtle import * #turtleをimport

def branch(length):#長さを入れてturtleさせる関数
    if length<10:
        return
    forward(length)#長さ分全身
    left(30)#30度左回転
    branch(length/2)#左の枝を回帰的に描く
    right(60)#60度右回転
    branch(length/2)#右の枝を回帰的に描く
    left(30)#30度左回転
    forward(-length)#長さ分戻る

branch(200)#今回は長さ200で開始

input()#turtleを描く