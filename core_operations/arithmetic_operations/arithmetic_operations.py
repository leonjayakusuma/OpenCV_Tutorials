import cv2 as cv
import numpy as np

# 1. 1D Array (interpreted as OpenCV Scalar)
# In OpenCV Python, 1D arrays with 1-4 elements are often treated as 'Scalar' (doubles).
# Scalars do NOT saturate because they use floating point math internally.
x = np.uint8([250])
y = np.uint8([10])
print("--- 1D Addition (Scalar behavior) ---")
print("cv.add(x, y):\n", cv.add(x, y)) # Likely [[260.] [0.] [0.] [0.]]
print("x + y (Numpy):", x + y)         # 4 (Overflow)

# 2. 2D Array (interpreted as OpenCV Mat/Image)
# When you have 2 dimensions, OpenCV treats it as a 'Mat' (image),
# and uint8 arithmetic WILL saturate at 255.
x2d = np.uint8([[250]])
y2d = np.uint8([[10]])
print("\n--- 2D Addition (Mat/Image behavior) ---")
print("cv.add(x2d, y2d):\n", cv.add(x2d, y2d)) # [[255]] (Saturated)

