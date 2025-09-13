from core.mouse_tracker import MouseTracker
from pynput import keyboard
from core.ui import FloatingWindow
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

        # if show_setting:
        #     window.show_settings()
        # else:
        #     window.hide_settings()

    # def on_release(key):
    #     # remove released key
    #     if key in pressed_keys:
    #         pressed_keys.remove(key)

    # ترد جدا برای کیبورد لیسنر (اختیاری)
    # threading.Thread(target=lambda: keyboard.Listener(on_press=on_press).join(), daemon=True).start()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # mainloop را در ترد اصلی اجرا کن
    window.mainloop()

if __name__ == "__main__":
    main()
