import cv2
import numpy as np

def apply_fourier_transform(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #grayscale
    dft = np.fft.fft2(gray)  
    dft_shift = np.fft.fftshift(dft)  #shift 0 freq to center
    return dft_shift, gray

def low_pass_filter(dft_shift, radius=30):
    rows, cols = dft_shift.shape
    crow, ccol = rows // 2 , cols // 2  #center

    mask = np.zeros((rows, cols), np.uint8)
    cv2.circle(mask, (ccol, crow), radius, 1, thickness=-1)  #circular mask

    dft_shift_filtered = dft_shift * mask
    return dft_shift_filtered

def high_pass_filter(dft_shift, radius=30):
    rows, cols = dft_shift.shape
    crow, ccol = rows // 2 , cols // 2 

    mask = np.ones((rows, cols), np.uint8)
    cv2.circle(mask, (ccol, crow), radius, 0, thickness=-1)  #inverse mask

    dft_shift_filtered = dft_shift * mask
    return dft_shift_filtered

def inverse_fourier_transform(dft_shift):
    dft_ishift = np.fft.ifftshift(dft_shift)  #Move zero frequency back
    img_back = np.fft.ifft2(dft_ishift) 
    img_back = np.abs(img_back) 
    return img_back

# Load image
img = cv2.imread("input.jpg")  

if img is None:
    print("Error: Image not found!")
else:
    dft_shift, gray = apply_fourier_transform(img)

    lpf_shift = low_pass_filter(dft_shift.copy(), radius=30)
    hpf_shift = high_pass_filter(dft_shift.copy(), radius=30)

    lpf_img = inverse_fourier_transform(lpf_shift)
    hpf_img = inverse_fourier_transform(hpf_shift)

    lpf_img = cv2.normalize(lpf_img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)   #so pixel between 0-255
    hpf_img = cv2.normalize(hpf_img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    cv2.imwrite("low_pass_filtered.jpg", lpf_img)
    cv2.imwrite("high_pass_filtered.jpg", hpf_img)

    cv2.imshow("Original", gray)
    cv2.imshow("Low Pass Filtered", lpf_img)
    cv2.imshow("High Pass Filtered", hpf_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()