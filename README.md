# Image-Text-Blurrer
This Python-based project aims to identify specific text within an image and apply a blurring effect to obscure it. The application utilises the Optical Character Recognition (OCR) capabilities of Tesseract, alongside the powerful image processing functionalities provided by OpenCV.

# Prerequisites
To run this project, you will need to install the following Python libraries:

- pytesseract
- opencv-python

You can install these using pip:
```pip install pytesseract opencv-python```

# Usage
```
img = cv2.imread('path_to_your_image.png')
// the text you want to find and blur
target_text = 'your_target_text'
blur_text(img, target_text)
```
Replace 'path_to_your_image.png' with the path to the image you want to process, and 'your_target_text' with the text you want to blur out.

# How it works
1. The script first uses pytesseract to perform OCR on the image and detect the text within it.
2. It iterates over each detected text element, and if the OCR's confidence is higher than a certain threshold, it checks whether the detected text contains the target text.
3. If the target text is found, the script then uses OpenCV to blur the corresponding region in the image.

# Limitations and Future Work
This project provides a basic implementation and may not perform well with complex images, such as those with varying fonts, rotations, and backgrounds, or low-quality images. Future enhancements could involve using machine learning to improve the robustness of the text detection and blurring process.

# Contributions
Please feel free to fork this project, open an issue, or submit a pull request if you want to contribute or suggest improvements!