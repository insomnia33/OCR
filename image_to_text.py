import pytesseract as ocr

from PIL import Image

phrase = ocr.image_to_string(Image.open('saoluis2.jpeg'), lang='por')

print(phrase)