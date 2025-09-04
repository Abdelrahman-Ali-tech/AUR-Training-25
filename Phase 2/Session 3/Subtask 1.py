import numpy as np
import matplotlib.pyplot as plt
import cv2

def convolve(image,kernel):
    k_l,k_w=kernel.shape
    if k_l%2 == 0 or k_w%2 == 0 :
        raise ValueError ("Kernl Dimensions must be odd")
    h_img,w_img=image.shape
    output=np.zeros((h_img,w_img))
    pad_h=k_l//2
    pad_w=k_w//2
    padded_img=np.pad(image,pad_width=((pad_h,pad_h),(pad_w,pad_w),),mode='constant',constant_values=0)
    filled_kernel=np.fliplr(np.flipud(kernel))
    for rows in range (image.shape[0]):
        for col in range (image.shape[1]):
            region=padded_img[rows:rows+k_l,col:col+k_w]
            output[rows,col]=np.sum(region*filled_kernel)
    return output        

img =cv2.imread(r'C:\Users\AliAl\Desktop\my python\AUR-Training-25\Phase 2\Session 3\image.jpg', cv2.IMREAD_GRAYSCALE)
fig, axes = plt.subplots(2, 2,figsize=(8, 8))

axes[0,0].imshow(img, cmap='gray')
axes[0,0].set_title('OriginalImage')
axes[0,0].axis('off')

axes[0,1].imshow(convolve(img, np.ones((5,5)) /25), cmap='gray')
axes[0,1].set_title('Box Filter')
axes[0,1].axis('off')

axes[1,0].imshow(convolve(img, np.array([[-1, 0, 1],[-2, 0,2], [-1,0, 1]])),
cmap='gray')
axes[1,0].set_title('HorizontalSobel Filter')
axes[1,0].axis('off')

axes[1,1].imshow(convolve(img, np.array([[-1,-2,-1],[0, 0,0], [1,2, 1]])),
cmap='gray')
axes[1,1].set_title('VerticalSobel Filter')
axes[1,1].axis('off')
plt.show()










