import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread("input.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found")
else:
    # Apply Histogram Equalization
    equalized_image = cv2.equalizeHist(image)

    # Compute histograms before and after equalization
    hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

    # Plot the original and equalized histograms
    plt.figure(figsize=(12, 5))

    # Original Image and Histogram
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.plot(hist_original, color='black')
    plt.title("Histogram (Before Equalization)")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    # Equalized Image and Histogram
    plt.subplot(2, 2, 3)
    plt.imshow(equalized_image, cmap='gray')
    plt.title("Histogram Equalized Image")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.plot(hist_equalized, color='black')
    plt.title("Histogram (After Equalization)")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    # Show the plots
    plt.tight_layout()
    plt.show()

    # Display images using OpenCV
    cv2.imshow("Original Image", image)
    cv2.imshow("Histogram Equalized Image", equalized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
