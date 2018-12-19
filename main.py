import cv2, pytesseract
from PIL import Image

def main():
    image = cv2.imread("img/test.png") # Add your image in the img folder and change this line to read your image.

    # Simple preprocessing to work in several images
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imshow('',gray)
    cv2.waitKey(0)

    # Save new image
    filename = "{}.png".format("temp")
    cv2.imwrite("img/" + filename, gray)

    # Open Image Using Tesseract
    text = pytesseract.image_to_string(Image.open("img/" + filename))
    print(text)

try:
    main()
except Exception as e:
    print(e.args)
    print(e.__cause__)
