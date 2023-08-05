import cv2
import numpy as np
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'tesseract path'


def blur_text(image, target_text):
    """Pytesseract's "image to data" function, which is Optical Character Reognition, 
    is used to recognise text in the image and return information about the text in a structured format.
    Output Dict is the structured format selected, which returns the output as a Python dictionary.
    """
    d = pytesseract.image_to_data(image, output_type=Output.DICT)

    n_boxes = len(d['text']) #calculating the number of text elements recognised using len. The next for loop then iterates over the recognised text elements.
    for i in range(n_boxes):
        # check if the OCR's confidence is greater than a threshold
        if int(d['conf'][i]) > 60:
            if target_text.lower() in d['text'][i].lower(): # convert detected text to lower case for case insensitive comparison
                # get the bounding box coordinates
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])


                # blur the area where the text is found. roi is the region of interest where the blurring takes place
                roi = image[y:y+h, x:x+w]
                blur = cv2.GaussianBlur(roi, (23, 23), 30)
                image[y:y+h, x:x+w] = blur
                
    cv2.imshow('Blurred Image', image)
    cv2.waitKey(0)

# load your image
img = cv2.imread('path_to_your_image.format')
# the text you want to find and blur
target_text = 'your_target_text'
blur_text(img, target_text)