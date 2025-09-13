# languages = ['en', 'fa']
# box_size = (20, 10) # x, y

# get data from setting.json
import json
import os

class Settings:
    def __init__(self):
        self.settings_path = os.path.join(os.path.dirname(__file__), 'setting.json')
        self.settings = {}
        self.load_settings()

    def load_settings(self):
        if not os.path.exists(self.settings_path):
            self.create_default_settings(self.settings_path)

        with open(self.settings_path, 'r', encoding='utf-8') as f:
            self.settings = json.load(f)

        return self

    
    def create_default_settings(self):
        default_settings = {
            "languages": [
                "en",
                "fa",
                "es",
                "fr",
                "de",
                "zh",
                "ar",
                "ru"
            ],
            "defaultLanguageInput": "en",
            "defaultLanguageOutput": "fa",
            "themes": [
                "light",
                "dark"
            ],
            "defaultTheme": "dark",
            "show_languages": {
                "en": "English", "fa": "فارسی", "es": "Español", 
                "fr": "Français", "de": "Deutsch", "zh": "中文",
                "ar": "العربية", "ru": "Русский"
            }
        }
        
        with open(self.settings_path, 'w', encoding='utf-8') as f:
            json.dump(default_settings, f, indent=4, ensure_ascii=False)
        self.settings = default_settings
        print(f"Default settings created at {self.settings_path}")


    def change_setting(self, key, value):
        if key in self.settings:
            self.settings[key] = value
            with open(self.settings_path, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=4, ensure_ascii=False)
            print(f"Setting '{key}' changed to '{value}'")
        else:
            print(f"Setting '{key}' does not exist.")

