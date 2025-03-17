#Aii v3.0
import keyboard
import time
import pyautogui
import pytesseract
from PIL import Image
import cv2
import numpy as np
import re

def screen():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    screenshot = pyautogui.screenshot()
    width, height = screenshot.size
    region = (width - int(width * 0.33), height - int(height * 0.33), width, height)
    cropped = screenshot.crop(region)
    gray = cropped.convert("L")
    gray_np = np.array(gray)
    _, thresh = cv2.threshold(gray_np, 200, 255, cv2.THRESH_BINARY)
    processed_image = Image.fromarray(thresh)
    raw_text = pytesseract.image_to_string(processed_image, config='--psm 6')
    no_parentheses_text = re.sub(r'\(.*?\)', '', raw_text)
    filtered_text = re.sub(r'[^A-Za-z\s]', '', no_parentheses_text)
    
    print("Texte détecté :", filtered_text)
    f= filtered_text
    return filtered_text

def send_messages(filtered_text):
    messages = [
        "/ano {* 1er sommation} {!#d4af37 partez sous peine de mourir du} " + filtered_text,
        "/ano {* 2eme sommation} {!#d4af37 partez sous peine de mourir du} " + filtered_text,
        "/ano {* 3eme sommation} {!#d4af37 partez sous peine de mourir du} " + filtered_text
    ]
    
    for msg in messages:
        keyboard.press_and_release('y')
        time.sleep(0.1)
        keyboard.write(msg)
        time.sleep(0.1)
        keyboard.press_and_release('enter')
        time.sleep(2)

while True:
    keyboard.wait('f12')
    filtered_text = screen()  
    send_messages(filtered_text)  
