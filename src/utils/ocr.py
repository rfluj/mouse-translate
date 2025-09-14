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
