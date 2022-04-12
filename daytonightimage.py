import numpy as np 
from imageio import imread,imwrite
import cv2
img=imread('samp.jpg')
a=img*np.array([0.1,0.2,0.5])
b=(255*a/a.max()).astype(np.uint8)
imwrite('night.jpg', b)
img2=cv2.imread('night.jpg')
gamma=2
gamma_img=np.array(255*(img2/255)**gamma,dtype='uint8')
cv2.imwrite('night_final.png',gamma_img)
