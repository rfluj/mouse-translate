import pyautogui
import easyocr
from PIL import Image
import numpy as np
import time

reader = easyocr.Reader(['en'])  # Add languages if needed

def get_text_under_mouse(box_size=(100, 20)):
    x, y = pyautogui.position()
    left = x - box_size[0] // 2
    top = y - box_size[1] // 2
    width, height = box_size

    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot_np = np.array(screenshot)

    # Save for debugging
    screenshot.save("debug_capture.png")

    results = reader.readtext(screenshot_np)
    print("OCR raw results:", results)

    text = " ".join([res[1] for res in results])
    return text

if __name__ == "__main__":
    print("Move your mouse to the text, waiting 3 seconds...")
    time.sleep(3)
    text = get_text_under_mouse()
    print("Detected text:", text)
