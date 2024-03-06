import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Cropping dynamic parts like the header and footer: adjust according to the device resolution
    cropped_image = gray_image[100:-100, :]
    return cropped_image

def compare_states(image1_path, image2_path, threshold=0.0015):
    image1 = preprocess_image(image1_path)
    image2 = preprocess_image(image2_path)
    # Calculate the difference and the comparison
    diff = cv2.absdiff(image1, image2)
    non_zero_count = np.count_nonzero(diff)
    diff_ratio = non_zero_count / diff.size
    return diff_ratio > threshold