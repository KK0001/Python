#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2

#imageをreadする
img = cv2.imread('God1.png',0)

#imageをshowする('windowの名前',開くimage)
cv2.imshow('image',img)
#〜millisecondsだけ表示
cv2.waitKey(0)
#windowを閉じる
cv2.destroyAllWindows()
