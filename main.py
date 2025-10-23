import customtkinter as ctk
from app.button import RedButton, YellowButton, GreenButton

from tkinter import filedialog, messagebox
import os
from collections import Counter

# Настройка внешнего вида
ctk.set_appearance_mode("System")  # "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

class FileAnalyzerApp(ctk.CTk):
    def __init__(self):
        super().__init__()  # Вызываем конструктор родительского класса (ctk.CTk)

        self.title("Проба пера")
        self.geometry("600x500")
        self.minsize(500, 400)
        self.iconbitmap("IMG/folder_icon.ico")

        self.create_widgets()

    def create_widgets(self):
        # Создаем кнопки используя наши классы
        red_button = RedButton(self)
        red_button.pack(pady=20)

        yellow_button = YellowButton(self)
        yellow_button.pack(pady=20)

        green_button = GreenButton(self)
        green_button.pack(pady=20)



if __name__ == "__main__":
    app = FileAnalyzerApp()
    app.mainloop()