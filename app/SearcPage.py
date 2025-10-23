import customtkinter as ctk
from .button import CustomButton
import tkinter as tk
from tkinter import filedialog


class SearchScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Сохраняем ссылку на главное приложение

        # Создаем виджеты экрана
        self.create_widgets()

    def create_widgets(self):
        """Создание всех виджетов экрана"""

        # Заголовок экрана
        self.title_label = ctk.CTkLabel(
            self,
            text="Анализ аудио файлов",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.pack(pady=20)

        # ========== ОБЛАСТЬ ДЛЯ КНОПОК ==========
        # Фрейм для кнопок
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.pack(fill="x", padx=20, pady=10)

        # === ОБЪЯВЛЕНИЕ КНОПКИ 1 ===
        self.button1 = CustomButton(
            self.buttons_frame,
            text="Кнопка 1",
            command=self.select_folder  # Привязываем функцию-обработчик
        )

        self.button1.pack(side="left", padx=10, pady=10)

        # === ОБЪЯВЛЕНИЕ КНОПКИ 2 ===
        self.button2 = CustomButton(
            self.buttons_frame,
            text="Кнопка 2",
            command=self.button2_clicked  # Привязываем функцию-обработчик
        )
        self.button2.pack(side="left", padx=10, pady=10)

        # === ОБЪЯВЛЕНИЕ КНОПКИ 3 ===
        self.button3 = CustomButton(
            self.buttons_frame,
            text="Кнопка 3",
            command=self.button3_clicked  # Привязываем функцию-обработчик
        )
        self.button3.pack(side="left", padx=10, pady=10)
        # ========== КОНЕЦ ОБЛАСТИ КНОПОК ==========

        # ========== ТЕКСТОВАЯ ПАНЕЛЬ ДЛЯ ИНФОРМАЦИИ О ФАЙЛАХ ==========
        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Заголовок текстовой панели
        self.info_label = ctk.CTkLabel(
            self.info_frame,
            text="Информация о файлах:",
            font=ctk.CTkFont(weight="bold")
        )
        self.info_label.pack(anchor="w", pady=(10, 5))

        # Сама текстовая панель (нередактируемая)
        self.info_text = ctk.CTkTextbox(
            self.info_frame,
            height=200
        )
        self.info_text.pack(fill="both", expand=True, pady=5)

        # Добавляем начальный текст "заглушка"
        self.info_text.insert("1.0", "заглушка")
        self.info_text.configure(state="disabled")  # Делаем недоступной для редактирования
        # ========== КОНЕЦ ТЕКСТОВОЙ ПАНЕЛИ ==========

    # ========== ФУНКЦИИ-ОБРАБОТЧИКИ КНОПОК ==========
    def select_folder(self):
        """
        Функция для выбора папки через диалоговое окно Windows
        """
        root = tk.Tk()
        root.withdraw()  # Скрываем окно (оно не будет видно пользователю)

        folder_path = filedialog.askdirectory(
            # Заголовок окна - что видит пользователь
            title="Выберите папку с аудио файлами",

            # Начальная директория - откуда начинается просмотр
            # "/" - корневая директория (в Windows это обычно C:\)
            initialdir="/",

            # Дополнительные параметры (необязательные):
            # mustexist=True - разрешить выбор только существующих папок
            # parent=root - привязка к нашему скрытому окну
        )
        # 4. УНИЧТОЖЕНИЕ СКРЫТОГО ОКНА (ОЧИСТКА ПАМЯТИ)
        root.destroy()

        # 5. ПРОВЕРКА РЕЗУЛЬТАТА
        if folder_path:
            # Если пользователь выбрал папку (не нажал "Отмена")
            print(f"Выбрана папка: {folder_path}")

            # Здесь можно добавить обработку выбранной папки:
            # - Сохранить путь в переменную
            # - Обновить интерфейс
            # - Просканировать файлы в папке

            return folder_path  # Возвращаем путь к выбранной папке
        else:
            # Если пользователь отменил выбор
            print("Выбор папки отменен")
            return None  # Возвращаем None чтобы показать что выбор отменен

    def button2_clicked(self):
        """Обработчик нажатия кнопки 2"""
        self.update_info_text("Нажата кнопка 2")

    def button3_clicked(self):
        """Обработчик нажатия кнопки 3"""
        self.update_info_text("Нажата кнопка 3")

    def update_info_text(self, message):
        """
        Обновляет текст на текстовой панели
        message: текст для отображения
        """
        # Разрешаем редактирование
        self.info_text.configure(state="normal")

        # Очищаем всё содержимое
        self.info_text.delete("1.0", "end")

        # Вставляем новый текст
        self.info_text.insert("1.0", message)

        # Снова делаем недоступной для редактирования
        self.info_text.configure(state="disabled")