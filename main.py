import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from collections import Counter

# Настройка внешнего вида
ctk.set_appearance_mode("System")  # "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

class FileAnalyzerApp(ctk.CTk):
    def __init__(self):
        super().__init__()  # Вызываем конструктор родительского класса (ctk.CTk)


    pass




if __name__ == "__main__":
    app = FileAnalyzerApp()
    app.mainloop()