import cv2

cam = cv2.VideoCapture(0)

res , img = cam.read()

if res:
    cv2.imshow("PIC",img)

    height, width, channels = img.shape
    num_pixels = height * width
    print(f"Image Dimensions: {width}x{height}")
    print(f"Total number of pixels: {num_pixels}")
    
    cv2.imwrite("imag.png",img)
    cv2.imwrite("image.jpg",img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No image detected")

cam.release()