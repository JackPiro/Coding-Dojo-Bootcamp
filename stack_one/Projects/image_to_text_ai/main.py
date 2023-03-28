import os
import pytesseract
from PIL import Image
import bs4

def extract_text_from_image(image_file):
    # Extract text from image using Tesseract
    text = pytesseract.image_to_string(Image.open(image_file))
    return text

def parse_text(text):
    # Parse text using Beautiful Soup
    soup = bs4.BeautifulSoup(text, 'html.parser')
    return soup

def create_html_file(soup, html_file):
    # Save parsed HTML to file
    with open(html_file, 'w') as f:
        f.write(str(soup))

def create_css_file(css_text, css_file):
    # Save CSS to file
    with open(css_file, 'w') as f:
        f.write(css_text)

def create_js_file(js_text, js_file):
    # Save JavaScript to file
    with open(js_file, 'w') as f:
        f.write(js_text)

def main(image_file, text_dir, html_dir, css_dir, js_dir):
    # Extract text from image
    text = extract_text_from_image(image_file)
    
    # Save text to file
    text_file = os.path.join(text_dir, 'wireframe.txt')
    with open(text_file, 'w') as f:
        f.write(text)
        
    # Parse text
    soup = parse_text(text)
    
    # Create HTML file
    html_file = os.path.join(html_dir, 'wireframe.html')
    create_html_file(soup, html_file)
    
    # Extract CSS from HTML
    css_text = soup.select('style')[0].text
    
    # Create CSS file
    css_file = os.path.join(css_dir, 'style.css')
    create_css_file(css_text, css_file)
    
    # Extract JavaScript from HTML
    js_text = soup.select('script')[0].text
    
    # Create JavaScript file
    js_file = os.path.join(js_dir, 'script.js')
    create_js_file(js_text, js_file)

if __name__ == "__main__":
    image_file = 'image/wireframe.png'
    text_dir = 'text'
    html_dir = 'html'
    css_dir = 'css'
    js_dir = 'js'
    main(image_file, text_dir, html_dir, css_dir, js_dir)
