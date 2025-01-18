
import cv2
import numpy as np

def scale_image(image, scale_factor):
    height, width, channels = image.shape
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    scaled_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            orig_x = int(i / scale_factor)
            orig_y = int(j / scale_factor)
            scaled_image[i, j] = image[orig_x, orig_y]

    return scaled_image

def rotate_image(image, angle):
    angle_rad = np.radians(angle)
    height, width, channels = image.shape
    center_x, center_y = height // 2, width // 2

    # empty array for the rotated image
    rotated_image = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            # Calculate the source coordinates
            x_shifted = i - center_x
            y_shifted = j - center_y

            src_x = int(center_x + (x_shifted * np.cos(angle_rad) - y_shifted * np.sin(angle_rad)))
            src_y = int(center_y + (x_shifted * np.sin(angle_rad) + y_shifted * np.cos(angle_rad)))

            # Check bounds 
            if 0 <= src_x < height and 0 <= src_y < width:
                rotated_image[i, j] = image[src_x, src_y]

    return rotated_image

def flip_image(image, flip_axis):
    height, width, channels = image.shape
    flipped_image = np.zeros_like(image)

    if flip_axis == 0:  # Vertical flip
        for i in range(height):
            flipped_image[i] = image[height - i - 1]

    elif flip_axis == 1:  # Horizontal flip
        for j in range(width):
            flipped_image[:, j] = image[:, width - j - 1]

    return flipped_image


image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
else:
    scaled_img = scale_image(image, 2)   
    rotated_img = rotate_image(image,90)    
    flipped_img = flip_image(image,0)      

    cv2.imshow("Original Image", image)
    cv2.imshow("Scaled Image", scaled_img)
    cv2.imshow("Rotated Image", rotated_img)
    cv2.imshow("Flipped Image", flipped_img)

    cv2.imwrite("scaled_image.jpg", scaled_img)
    cv2.imwrite("rotated_image.jpg", rotated_img)
    cv2.imwrite("flipped_image.jpg", flipped_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
