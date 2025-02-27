import cv2
import numpy as np

# Load the image
image = cv2.imread("shapes.jpeg")

# Check if image is loaded properly
if image is None:
    print("Error: Image not found or cannot be loaded. Check the file path.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur

# Perform edge detection
edges = cv2.Canny(blurred, 50, 150)

# Find contours in the edged image
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop through contours and detect shapes
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)  # Approximate the contour
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)  # Draw the detected shape

    # Get the bounding rectangle for text placement
    x, y, w, h = cv2.boundingRect(approx)
    
    # Identify the shape based on the number of sides
    if len(approx) == 3:
        shape_name = "Triangle"
    elif len(approx) == 4:
        aspect_ratio = w / float(h)
        shape_name = "Square" if 0.95 <= aspect_ratio <= 1.05 else "Rectangle"
    elif len(approx) > 4:
        shape_name = "Circle"
    else:
        shape_name = "Unknown"

    # Adjust text position dynamically
    text_x = x + w // 2 - 30  # Center horizontally
    text_y = y + h + 20  # Place text slightly below the shape

    cv2.putText(image, shape_name, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)

# Display the image with detected shapes
cv2.imshow("Detected Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
