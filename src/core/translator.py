from googletrans import Translator


class Translate:
    def __init__(self):
        self._translator = Translator()
    
    def _translate_text(self, text, lang):
        if not text:
            return ''
        try:
            translated = self._translator.translate(text, dest=lang)
            return translated.text
        except Exception as e:
            print("خطا در ترجمه:", e)
            return ''

# t = Translate()
# print(t._translate_text("fine", "fa"))