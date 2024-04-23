import cv2
import numpy as np
from matplotlib import pyplot as plt

#Load images
img1 = cv2.imread('a1.jpg')
img2 = cv2.imread('a2.jpg')
img3 = cv2.imread('a3.jpg')

#Check if there're errors when loading images
if img1 is None:
    print('Error: Cannot read image a1.jpg')
    exit(1)
if img2 is None:
    print('Error: Cannot read image a2.jpg')
    exit(1)
if img3 is None:
    print('Error: Cannot read image a3.jpg')
    exit(1)

# Stitch images together
stitcher = cv2.Stitcher_create()
status, panorama = stitcher.stitch((img1, img2, img3))

# Check if stitching is successful
if status == cv2.Stitcher_OK:
    plt.figure(figsize=(15, 5))
    plt.imshow(cv2.cvtColor(panorama, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.savefig('Export.png', dpi=300, bbox_inches='tight')
    plt.show()
else:
    print("Stitching unsuccessful, try again")
