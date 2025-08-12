import tkinter as tk

class FloatingWindow:
    def __init__(self):
        self._root = tk.Tk()
        self._root.overrideredirect(True)
        self._root.attributes("-topmost", True)
        self._root.withdraw()

        self._label = tk.Label(self._root, text="", bg="yellow", fg="black", font=("Arial", 10))
        self._label.pack()

    def show(self, text, pos):
        # چون ممکنه show از ترد غیر اصلی صدا زده شود، با after به ترد اصلی ارسال می‌کنیم
        self._root.after(0, self._show_ui, text, pos)

    def _show_ui(self, text, pos):
        x, y = pos
        self._label.config(text=text)
        self._root.geometry(f"+{x}+{y + 20}")
        if not self._root.winfo_viewable():
            self._root.deiconify()

    def hide(self):
        self._root.after(0, self._root.withdraw)

    def mainloop(self):
        self._root.mainloop()
