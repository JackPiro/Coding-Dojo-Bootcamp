import pytesseract
from PIL import Image

def extract_text_from_image(image_file):
    # Open image file
    image = Image.open(image_file)
    
    # Extract text from image
    text = pytesseract.image_to_string(image)
    
    return text
