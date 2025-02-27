import cv2
import numpy as np

# Load the image
image = cv2.imread("image.jpg")

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Make a copy of the image to add watermark
watermarked_img = image.copy()

# Define watermark text properties
watermark_text = "WOODSTOCK"
position = (500, 600)  # (x, y) position of watermark
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 4  # Large font size
color = (100, 100, 100)  # Light gray watermark
thickness = 10

# Add the watermark (large, visible gray text)
cv2.putText(watermarked_img, watermark_text, position, font, 
            font_scale, color, thickness, cv2.LINE_AA)

# Save and display the watermarked image
cv2.imwrite("watermarked_img.jpg", watermarked_img)
cv2.imshow("Watermarked Image", watermarked_img)
cv2.waitKey(0)

# ---- Step 2: Remove Watermark Using Inpainting ----
# Create a mask for the watermark
mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.putText(mask, watermark_text, position, font, 
            font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

# Apply inpainting to remove the watermark
inpainted_img = cv2.inpaint(watermarked_img, mask, 5, cv2.INPAINT_TELEA)

# Save and display the final image
cv2.imwrite("watermark_removed.jpg", inpainted_img)
cv2.imshow("Watermark Removed", inpainted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
