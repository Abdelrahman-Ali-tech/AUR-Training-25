import numpy as np
import matplotlib.pyplot as plt
import cv2
img =cv2.imread(r'C:\Users\AliAl\Desktop\my python\AUR-Training-25\Phase 2\Session 3\shapes.jpg')
out =img.copy()
red_mask=cv2.inRange(img,(200,0,0),(255,50,50))
black_mask=cv2.inRange(img,(0,0,0),(50,50,50))
blue_mask=cv2.inRange(img,(0,0,200),(50,50,255))
out[blue_mask>0]=(0,0,0)
out[red_mask>0]=(0,0,255)
out[black_mask>0]=(255,0,0)


fig, axes = plt.subplots(1, 2)
axes[0].imshow(img)
axes[0].set_title('OriginalImage')
axes[0].axis('off')

axes[1].imshow(out)
axes[1].set_title('ProcessedImage')
axes[1].axis('off')

plt.show()