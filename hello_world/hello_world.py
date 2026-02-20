import cv2 as cv
import numpy as np
import os

print("OpenCV:", cv.__version__)
img = np.zeros((120, 400, 3), dtype=np.uint8)
cv.putText(img, "OpenCV OK", (10, 80), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "output")

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save to the specific output directory
output_path = os.path.join(output_dir, "hello.png")
success = cv.imwrite(output_path, img)

if success:
    print(f"Image saved successfully to: {output_path}")
else:
    print("Failed to save image.")
