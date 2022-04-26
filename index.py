# Import required packages
import cv2
import pytesseract
import json
class Person:
    def __init__(self, hoten , socd , ngaysinh , address1 , address2):
        self.hoten = hoten
        self.socd = socd
        self.ngaysinh = ngaysinh
        self.address1 = address1
        self.address2 = address2

def readImg(urls):
    # Mention the installed location of Tesseract-OCR in your system
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    persons  = []
    # Read image from which text needs to be extracted
    for url in urls :
        print(url)
        img = cv2.imread(url)
        identify = img[30:115,85:255];
        text = pytesseract.image_to_string(identify, lang="vie");
        if(text != ""):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            socd = img[180:222, 700:970];
            hoten = img[230:270,580:1080]
            ngaysinh = img[285:320,780:950]
            address_1 =  img[385:420, 600:1080]
            address_2 = img[420:455 , 420:1080]
            text_socd = pytesseract.image_to_string(socd, lang="vie");
            text_hoten = pytesseract.image_to_string(hoten, lang="vie");
            text_ngaysinh = pytesseract.image_to_string(ngaysinh, lang="vie");
            text_address_1 = pytesseract.image_to_string(address_1, lang="vie");
            text_address_2 = pytesseract.image_to_string(address_2, lang="vie");

            person1 = Person(text_hoten,text_socd,text_ngaysinh,text_address_1,text_address_2)
            persons.append(person1)

    return persons;