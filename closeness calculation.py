

import pandas as pd
import numpy as np
import cv2

cap= cv2.VideoCapture(r'/content/Test.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(str(i)+'.jpg',frame)
    i+=1
cv2.destroyAllWindows()
cap.release()

def entropy_cal(path):
  src=cv2.imread(path)
  gimg = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  x=pd.DataFrame(gimg.reshape(-1,1))
  
  f=x.value_counts(normalize=True)
  h=[]
  en=0
  for i in f:
    h.append(float(i))

  for i in h:
    b=np.log2(i)
    c=b*i
    en=en-c
  return en

from google.colab.patches import cv2_imshow
from termcolor import colored
for i in range (0,200,30):
  string=str(i)+'.jpg'
  print("entropy of frame no.",i,':',entropy_cal(string))
  img1=cv2.imread(string)
  cv2_imshow(img1)
  print('\n\n')
