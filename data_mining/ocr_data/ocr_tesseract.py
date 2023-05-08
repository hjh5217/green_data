"""
이미지에 있는 텍스트 추출
Tesseract - OCR 프로그램 중 하나
다양한 운영체제에서 사용할 수 있는 엔진
"""

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open("news.png"), lang="kor")
#print(text)
print(text.replace(" ", ""))

"""
with open("news.txt", 'w', encoding='utf8') as f:
    f.write(text)
    f.write("\n\n\n")
    f.write(text.replace(' ', ''))
"""