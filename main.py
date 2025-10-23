import customtkinter as ctk
from app.SearcPage import SearchScreen

ctk.set_appearance_mode("System")  # "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"


class FileAnalyzerApp(ctk.CTk):
    def __init__(self):
        super().__init__()  # Вызываем конструктор родительского класса

        # Настройка главного окна
        self.title("Проба пера")
        self.geometry("600x500")
        self.minsize(500, 400)
        self.iconbitmap("IMG/folder_icon.ico")

        # Создаем контейнер для экранов
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)

        # Показываем стартовый экран
        self.show_search_screen()

    def show_search_screen(self):
        """Показать экран поиска файлов"""
        # Создаем экран поиска
        search_screen = SearchScreen(self.container, self)
        search_screen.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = FileAnalyzerApp()
    app.mainloop()