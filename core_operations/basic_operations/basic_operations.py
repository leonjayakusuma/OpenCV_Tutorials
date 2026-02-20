import numpy as np
import cv2 as cv
import os

# Get path relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'messi5.jpg')

img = cv.imread(image_path)
assert img is not None, f"file could not be read from: {image_path}"

# image properties
print(img.shape)
print(img.size)
print(img.dtype)

rows, cols, channels = img.shape
print(f"Image dimensions: {rows}x{cols}x{channels}")

# image roi (Region of Interest)
# Adjusted for a 280x450 image (the original tutorial assumes 342x548)
# We'll pick a safe ROI within the bounds of your image.
# If this is the Messi image, the ball is roughly around these coordinates:
ball_y1, ball_y2 = 230, 275
ball_x1, ball_x2 = 270, 315

# Ensure ROI is within image bounds
ball_y2 = min(ball_y2, rows)
ball_x2 = min(ball_x2, cols)

ball = img[ball_y1:ball_y2, ball_x1:ball_x2]
print(f"ROI shape: {ball.shape}")

# Only attempt to copy if the ROI is not empty
if ball.size > 0:
    # Target location to copy the 'ball' to
    # Ensure target bounds are also valid
    target_y1, target_y2 = 200, 200 + (ball_y2 - ball_y1)
    target_x1, target_x2 = 100, 100 + (ball_x2 - ball_x1)
    
    if target_y2 <= rows and target_x2 <= cols:
        img[target_y1:target_y2, target_x1:target_x2] = ball
        print(f"Successfully copied ROI to [{target_y1}:{target_y2}, {target_x1}:{target_x2}]")
    else:
        print("Target ROI out of bounds.")
else:
    print("Source ROI is empty. Check your coordinates.")

# Show result or save
output_dir = os.path.join(script_dir, 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, 'roi_result.png')
success = cv.imwrite(output_path, img)

if success:
    print(f"Result saved successfully to: {output_path}")
else:
    print(f"Failed to save result to: {output_path}")



b,g,r = cv.split(img)

# Create output directory
output_dir = os.path.join(script_dir, 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save each channel
cv.imwrite(os.path.join(output_dir, 'blue_channel.png'), b)
cv.imwrite(os.path.join(output_dir, 'green_channel.png'), g)
cv.imwrite(os.path.join(output_dir, 'red_channel.png'), r)

print("Channels saved successfully to output directory.")

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

# Create output directory
output_dir = os.path.join(script_dir, 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save each channel
cv.imwrite(os.path.join(output_dir, 'blue_channel.png'), b)
cv.imwrite(os.path.join(output_dir, 'green_channel.png'), g)
cv.imwrite(os.path.join(output_dir, 'red_channel.png'), r)

print("Channels saved successfully to output directory.")

img[:,:,2] = 0

# Create output directory
output_dir = os.path.join(script_dir, 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save each channel
cv.imwrite(os.path.join(output_dir, 'new_messi.png'), img)


print("New image saved successfully to output directory.")

