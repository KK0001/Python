import cv2
import numpy as np

img = cv2.imread("ファイル名1")
mask = np.zeros(img.shape[:2],np.uint8)
skyimg = cv2.resize(cv2.imread("ファイル名2"),
                         img.shape[1::-1])
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (0,0,img.shape[1],round(img.shape[0]*0.7))
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,
                      50,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
mask2 = cv2.blur(mask2,(5,5))
img2 = img*(1-mask2[:,:,np.newaxis])
skyimg = skyimg*mask2[:,:,np.newaxis]
img3 = cv2.addWeighted(skyimg, 1, img2, 1, 2.5)
cv2.imwrite("out.jpg",img3)
cv2.imshow("preview",img3)
cv2.waitKey()
