import cv2
import numpy as np


image=cv2.imread('img/image.png')
img_float = image.astype(np.float32)
min_val = np.min(img_float)
max_val = np.max(img_float)
stretched = (img_float - min_val) * (255 / (max_val - min_val))
stretched = np.clip(stretched, 0, 255).astype(np.uint8)
cv2.imshow("strtched",stretched)