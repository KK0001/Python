# -*- coding: utf-8 -*-

#動画から顔認識をしたい。

import cv2
import time

#HAAR分類器の顔検出用の特徴量
#cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
#cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
#cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml"
#cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml"
cascade_path = "../lib/lbpcascade_animeface/lbpcascade_animeface.xml"

video_path = "../Desktop/yuyusiki_op.mp4
out_video_path = "../Desktop/face_yuyusiki_op.avi"

color = (0,255,0) #Green

#カスケード分類器の特徴量を取得する
cascade = cv2.CascadeClassifier(cascade_path)

# 動画のエンコード　とりあえず、これで動く拡張子はm4vで
fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
# 動画ファイル読み込み
cap = cv2.VideoCapture(video_path)

#書き込み先("書き込み先の名前",エンコード,FPS,解像度)
out = cv2.VideoWriter("face_output.m4v", fourcc, 30.0, (1280,720))

#初期値の宣言
frame_num = 0
img_cnt = 0
# フレームごとの処理
while(cap.isOpened()):#動画のフレームが無くなるまでループ
  ret, frame = cap.read()#ret,frameにcap.read()を収納
  if (ret == False):#動画のフレームが無かったらbreak
    break

  #グレースケール変換
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #顔認証？
  facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighb  ors=1, minSize=(1, 1))

  print("frame : %d" % frame_num)#フレームを表示
  if len(facerect) &gt; 0:#顔が見つかった時
    #検出した顔を囲む矩形の作成
    for (x,y,w,h) in facerect:#
    cv2.rectangle(frame, (x,y),(x+w,y+h), color, thickness=7)
    img_cnt += 1
  out.write(frame)
  frame_num += 1

cap.release()#読み込みをやめます
cv2.destroyAllWindows()#windowを閉じる
out.release()#書き込み先を閉じます
