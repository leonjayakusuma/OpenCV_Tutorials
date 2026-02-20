import cv2 as cv
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img1 = cv.imread(os.path.join(script_dir, 'ml.png'))
img2 = cv.imread(os.path.join(script_dir, 'opencv_logo.png'))
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"

# Resize img2 to match img1 dimensions (requirement for cv.addWeighted)
img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))

dst = cv.addWeighted(img1,0.7,img2,0.3,0)

# Create output directory and save the result
output_dir = os.path.join(script_dir, 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, 'blended_result.png')
cv.imwrite(output_path, dst)
print(f"Blended result saved to: {output_path}")

# Comment out imshow for now to avoid blocking if the user is in a headless environment
# cv.imshow('dst',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()
