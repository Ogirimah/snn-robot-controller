import cv2
import numpy as np

# Load images into a list
image_files = ['image1.jpg', 'image2.jpg', 'image3.jpg']  # Add your image paths
images = [cv2.imread(img) for img in image_files]

# Convert images to grayscale
gray_images = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in images]

# Initialize an empty list to store filtered images
filtered_images = []

# Define a simple temporal filter (e.g., averaging filter)
for i in range(1, len(gray_images) - 1):
    filtered_image = cv2.addWeighted(gray_images[i-1], 0.33, gray_images[i], 0.34, 0)
    filtered_image = cv2.addWeighted(filtered_image, 1, gray_images[i+1], 0.33, 0)
    filtered_images.append(filtered_image)

# Save or display the filtered images
for idx, img in enumerate(filtered_images):
    cv2.imwrite(f'filtered_image_{idx}.jpg', img)
    cv2.imshow(f'Filtered Image {idx}', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
