import numpy as np
import matplotlib.pyplot as plt

img=plt.imread("C:\\Users\\student\\Downloads\\tiger.png")
img=img[:,:,0].copy()

plt.figure(1)
plt.imshow(img,cmap="gray")

img_array=[]

img_array=img+0.6
img_array[img_array>1]=1

plt.figure(2)
plt.imshow(img_array,cmap='gray')

rotated= np.rot90(img, 1)

plt.figure(3)
plt.imshow(rotated,cmap='gray')

mirror=np. fliplr(img)

plt.figure(4)
plt.imshow(mirror,cmap='gray')

resize=img[::10,::10]

plt.figure(5)
plt.imshow(resize,cmap='gray')

redovi = img.shape[0] 
stupci = img.shape[1] 
dg = stupci//4
gg = stupci//2

pr_img = img.copy()
for i in range(redovi):
    for j in range(stupci):
        if (j < dg or j > gg): 
            pr_img[i][j] = 0

plt.figure(6)
plt.imshow(pr_img,cmap='gray')

plt.show()


