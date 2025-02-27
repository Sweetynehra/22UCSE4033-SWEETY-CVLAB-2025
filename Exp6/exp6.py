import cv2
import numpy as np

# Load medical image (grayscale)
image = cv2.imread("medical.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur to reduce noise
    blurred_img = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred_img, 50, 150)

    # Display images
    cv2.imshow("Original Medical Image", image)
    cv2.imshow("Edge Detected Image", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the result
    cv2.imwrite("edge_detected.jpg", edges)
