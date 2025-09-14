from src.core import MouseTracker, FloatingWindow
from pynput import keyboard
import threading

def main():
    window = FloatingWindow()
    tracker = MouseTracker(window)  # به MouseTracker پنجره را بدهیم

    # pressed_keys = set()
    
    def on_press(key):
        # pressed_keys.add(key)
        if key == keyboard.Key.f7:
            if tracker.is_running:
                print("توقف ردیابی موس")
                tracker.stop()
                window.hide()
            window.setting()
        
        elif key == keyboard.Key.f8:
            if tracker.is_running:
                print("توقف ردیابی موس")
                tracker.stop()
                window.hide()
            else:
                print("شروع ردیابی موس")
                tracker.start()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # mainloop را در ترد اصلی اجرا کن
    window.mainloop()

if __name__ == "__main__":
    main()
