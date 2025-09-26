import pytesseract
from PIL import Image

def extract_text(img_path):
    try:
        text = pytesseract.image_to_string(Image.open(img_path))
        return text.strip()
    except Exception as e:
        return f"Erreur OCR : {str(e)}"