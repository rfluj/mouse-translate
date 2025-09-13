import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


class FloatingWindow:
    def __init__(self):
        self.settings_file = "setting.json"
        self.settings = self.load_settings()
        self._root = tk.Tk()
        self._root.overrideredirect(True)
        self._root.attributes("-topmost", True)
        self._root.withdraw()
        self.dark_bg_color = "#010F09"
        self.dark_text_color = "#010F09"
        self.dark_bt_color = "#010F09"
        self.light_bg_color = "#E9F0ED"
        self.light_bt_color = "#E9F0ED"
        self.light_text_color = "#E9F0ED"

        self._label = tk.Label(self._root, text="", font=("Arial", 10))
        # self._label.pack()

        self.show_setting = False

    def show(self, text, pos):
        # چون ممکنه show از ترد غیر اصلی صدا زده شود، با after به ترد اصلی ارسال می‌کنیم
        self._root.after(0, self._show_ui, text, pos)

    def _show_ui(self, text, pos):
        x, y = pos
        if self.settings['defaultTheme'] == 'dark':
            self._label.config(bg=self.dark_bg_color, fg=self.light_text_color)
            # self._label = tk.Label(self._root, text="", bg="#010F09", fg="#E9F0ED", font=("Arial", 10))
        else:
            self._label.config(bg=self.light_bg_color, fg=self.dark_text_color)
        self._label.pack()
        self._label.config(text=text)
        self._root.geometry(f"+{x}+{y + 20}")
        if not self._root.winfo_viewable():
            self._root.deiconify()

    def hide(self):
        self._root.after(0, self._root.withdraw)

    def mainloop(self):
        self._root.mainloop()

    def setting(self):
        if self.show_setting:
            self.hide_settings()
            self.show_setting = False
        else:
            self.show_settings()
            self.show_setting = True
    
    def load_settings(self):
        default_settings = {
            "languages": ["en", "fa", "es", "fr", "de", "zh", "ar", "ru"],
            "defaultLanguageInput": "fa",
            "defaultLanguageOutput": "en",
            "themes": ["light", "dark"],
            "defaultTheme": "light"
        }
        
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                # Create default settings file if it doesn't exist
                with open(self.settings_file, 'w', encoding='utf-8') as f:
                    json.dump(default_settings, f, indent=4)
                return default_settings
        except Exception as e:
            print(f"Error loading settings: {e}")
            return default_settings
            
    def save_settings(self):
        try:
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("successful", "setting changed successfully", parent=self._root)
            return True
        except Exception as e:
            messagebox.showerror("error", f"get some error in changing setting: {e}", parent=self._root)
            return False

    def show_settings(self):
        lang_names = {
            "en": "English", "fa": "فارسی", "es": "Español", 
            "fr": "Français", "de": "Deutsch", "zh": "中文",
            "ar": "العربية", "ru": "Русский"
        }

        window = tk.Toplevel(self._root)
        window.title("setting")
        window.geometry("400x350")
        # label = tk.Label(window, text="setting")
        # label.pack(pady=20)
        change_input_lang_label_text = "change input language"
        change_input_lang_label = tk.Label(window, text=change_input_lang_label_text)
        change_input_lang_label.pack(pady=5)

        input_lang_label_text = lang_names[self.settings['defaultLanguageInput']]
        input_lang_label = tk.Label(window, text=input_lang_label_text)
        input_lang_label.pack(pady=5)
        self.input_lang = tk.StringVar(value=self.settings["defaultLanguageInput"])
        
        
        input_combo = ttk.Combobox(input_lang_label, textvariable=self.input_lang, 
                                  values=[f"{code} - {lang_names.get(code, code)}" for code in self.settings["languages"]],
                                  state="readonly", width=30)
        input_combo.pack(pady=5)

        change_output_lang_label_text = "change output language"
        change_output_lang_label = tk.Label(window, text=change_output_lang_label_text)
        change_output_lang_label.pack(pady=5)

        output_lang_label_text = lang_names[self.settings['defaultLanguageOutput']]
        output_lang_label = tk.Label(window, text=output_lang_label_text)
        output_lang_label.pack(pady=5)
        self.output_lang = tk.StringVar(value=self.settings["defaultLanguageOutput"])
        
        
        output_combo = ttk.Combobox(output_lang_label, textvariable=self.output_lang, 
                                  values=[f"{code} - {lang_names.get(code, code)}" for code in self.settings["languages"]],
                                  state="readonly", width=30)
        output_combo.pack(pady=5)

        # Theme selection
        theme_frame = tk.Label(window, text="theme")
        theme_frame.pack(pady=5)
        
        self.theme_var = tk.StringVar(value=self.settings["defaultTheme"])
        theme_combo = ttk.Combobox(theme_frame, textvariable=self.theme_var,
                                  values=self.settings["themes"], state="readonly", width=30)
        theme_combo.pack(pady=5)
        
        # Buttons frame
        button_frame = ttk.Frame(window)
        button_frame.pack(pady=5)

        # Save button
        save_btn = tk.Button(button_frame, text="save", command=self.on_save,
                            bg="#27ae60", fg="white", font=("Tahoma", 10), padx=15, pady=5)
        save_btn.pack(side=tk.RIGHT, padx=10)
        
        # Cancel button
        cancel_btn = tk.Button(button_frame, text="cancel", command=window.destroy,
                              bg="#e74c3c", fg="white", font=("Tahoma", 10), padx=15, pady=5)
        cancel_btn.pack(side=tk.LEFT, padx=10)


        # change_lang_entry = tk.Entry(window)
        # change_lang_entry.pack(pady=5)
        # change_lang_button = tk.Button(window, text="تغییر", command=lambda: print(f"زبان تغییر یافت به: {change_lang_entry.get()}"))
        # change_lang_button.pack(pady=5)
        # change_theme_label = tk.Label(window, text="تغییر تم:")
        # change_theme_label.pack(pady=10)
        # change_theme_entry = tk.Entry(window)
        # change_theme_entry.pack(pady=5)
        # change_theme_button = tk.Button(window, text="تغییر", command=lambda: print(f"تم تغییر یافت به: {change_theme_entry.get()}"))
        # change_theme_button.pack(pady=5)

        # close = tk.Button(window, text="بستن", command=window.destroy)
        # close.pack(pady=10)
        # print("پنجره تنظیمات نمایش داده شد")

    def on_save(self):
        # Extract language codes from combobox values
        input_code = self.input_lang.get().split(" - ")[0]
        output_code = self.output_lang.get().split(" - ")[0]
        
        # Update settings
        self.settings["defaultLanguageInput"] = input_code
        self.settings["defaultLanguageOutput"] = output_code
        self.settings["defaultTheme"] = self.theme_var.get()
        
        self.save_settings()
        # # Save to file
        # if self.save_settings():
        #     self._root.destroy()

    def hide_settings(self):
        for widget in self._root.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()
        print("پنجره تنظیمات مخفی شد")
