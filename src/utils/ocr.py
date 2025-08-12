import pyautogui
import pyperclip
import time

def get_text_under_mouse(x, y):
    # حرکت موس به موقعیت
    pyautogui.moveTo(x, y)
    
    # کلیک چپ برای فعال کردن مکان
    pyautogui.doubleClick()
    # time.sleep(0.1)
    
    # شبیه‌سازی Ctrl+C برای کپی متن انتخاب شده
    pyautogui.hotkey('ctrl', 'c')
    # time.sleep(0.1)  # کمی مکث برای ثبت شدن در کلیپ‌بورد
    
    # دریافت متن از کلیپ‌بورد
    text = pyperclip.paste()
    return text

# # تست
# if __name__ == "__main__":
#     print("شروع تست کپی متن زیر موس...")
#     try:
#         while True:
#             x, y = pyautogui.position()
#             text = get_text_under_mouse(x, y)
#             print(f"موقعیت موس: {x}, {y}  متن: {text}")
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("برنامه متوقف شد.")




# import easyocr
# from PIL import ImageGrab
# import time
# import numpy as np
# from config import *


# def get_text_under_mouse(x, y, box_size=box_size, languages=languages):
#     left = x - box_size[0] // 2
#     top = y - box_size[1] // 2
#     right = x + box_size[0] // 2
#     bottom = y + box_size[1] // 2

#     img = ImageGrab.grab(bbox=(left, top, right, bottom))
#     img_np = np.array(img)

#     reader = easyocr.Reader(languages)

#     result = reader.readtext(img_np, detail=0)
#     return ' '.join(result)

# # def main():
# #     print("شروع تست EasyOCR زیر موس. برای خروج Ctrl+C بزنید.")
# #     try:
# #         while True:
# #             text = get_text_under_mouse()
# #             print(f"موقعیت موس: متن زیر موس: '{text}'")
# #             time.sleep(0.5)
# #     except KeyboardInterrupt:
# #         print("برنامه متوقف شد.")

# # if __name__ == "__main__":
# #     main()
