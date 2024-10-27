import os
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

required_key_names = ['gender_value','dob_value','adhar_number_value','name_value']
crops_path = 'govt_id/adhaar/crops'




def process_crops():

    result = {
        "gender_value":"",
        "dob_value":"",
        "adhar_number_value":"",
        "name_value":""
    }
    for name in os.listdir(crops_path):
        if name in required_key_names:
            image_path = crops_path + '/' + name + '/image.jpg'
            if os.path.exists(image_path):
                result[name] = run_ocr(image_path)
            else:
                print(False)

    return result



def run_ocr(image_path):
    
    image = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(image)

    # Print the extracted text
    print(text)

    return text
