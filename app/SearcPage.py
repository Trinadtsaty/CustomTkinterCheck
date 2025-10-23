import customtkinter as ctk
from .button import CustomButton
import tkinter as tk
from tkinter import filedialog
import os
import json
from pathlib import Path


class SearchScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Сохраняем ссылку на главное приложение
        self.folder_path = None
        self.audio_list_path = "file/audio_list.json"
        self.metafate_path = "file/metadate.json"

        # Создаем виджеты экрана
        self.create_widgets()
        self.check_folder()

    def check_folder(self):
        """
        Проверяет существование ключевых файлов и создает их если нужно
        """
        # Создаем папку если не существует
        folder = os.path.dirname(self.audio_list_path)
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Создана папка: {folder}")

        # Проверяем и создаем audio_list.json если нужно
        if not os.path.exists(self.audio_list_path):
            with open(self.audio_list_path, 'w', encoding='utf-8') as f:
                json.dump({}, f)  # Пустой список
            print(f"Создан файл: {self.audio_list_path}")
        else:
            print(f"Файл уже существует: {self.audio_list_path}")

        # Проверяем и создаем metadate.json если нужно
        if not os.path.exists(self.metafate_path):
            # Данные для метаданных
            metadata_template = {
                "metadata": {
                    "\\xa9nam": "Название трека (Title)",
                    "\\xa9ART": "Исполнитель (Artist)",
                    "\\xa9alb": "Альбом (Album)",
                    "trkn": "Номер трека (Track number)",
                    "disk": "Номер диска (Disc number)",
                    "\\xa9day": "Год выпуска (Year)",
                    "\\xa9gen": "Жанр (Genre)",
                    "\\xa9wrt": "Композитор (Composer)",
                    "aART": "Исполнитель альбома (Album Artist)",
                    "\\xa9too": "Программа кодирования (Encoding software)",
                    "\\xa9cmt": "Комментарий (Comment)"
                }
            }

            with open(self.metafate_path, 'w', encoding='utf-8') as f:
                json.dump(metadata_template, f, ensure_ascii=False, indent=2)
            print(f"Создан файл: {self.metafate_path}")
        else:
            print(f"Файл уже существует: {self.metafate_path}")

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
            text="Укажите путь",
            command=self.select_folder  # Привязываем функцию-обработчик
        )

        self.button1.pack(side="left", padx=10, pady=10)

        # === ОБЪЯВЛЕНИЕ КНОПКИ 2 ===
        self.button2 = CustomButton(
            self.buttons_frame,
            text="Анализ",
            command=self.create_audio_list  # Привязываем функцию-обработчик
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

        self.folder_path = filedialog.askdirectory(
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
        if self.folder_path:

            # Если пользователь выбрал папку (не нажал "Отмена")
            print(f"Выбрана папка: {self.folder_path}")

            # Здесь можно добавить обработку выбранной папки:
            # - Сохранить путь в переменную
            # - Обновить интерфейс
            # - Просканировать файлы в папке
            self.update_info_text(self.folder_path)
            return self.folder_path  # Возвращаем путь к выбранной папке
        else:
            # Если пользователь отменил выбор
            print("Выбор папки отменен")
            return None  # Возвращаем None чтобы показать что выбор отменен



    def create_audio_list(self):
        print("Функция вызвана")
        audio_files = {}
        counter = 1

        print(self.folder_path)
        for file in os.listdir(self.folder_path):
            print(os.listdir(self.folder_path))
            print(file)
            print(file.lower().endswith(('.mp3', '.m4a')))
            if file.lower().endswith(('.mp3', '.m4a')):
                name, extension = os.path.splitext(file)
                # file_stem = Path(file).stem
                audio_files[str(counter)] = {
                    "file_name": name,
                    "file_extension":extension,
                    "metadata": {
                        "\\xa9nam": name,  # Название трека (Title) str
                        "\\xa9ART": None,  # Исполнитель (Artist) str
                        "\\xa9alb": None,  # Альбом (Album) str
                        "trkn": None,  # Номер трека (Track number) tuple
                        "disk": None,  # Номер диска (Disc number) tuple
                        "\\xa9day": None,  # Год выпуска (Year) str
                        "\\xa9gen": None,  # Жанр (Genre) str
                        "\\xa9wrt": None,  # Композитор (Composer) str
                        "aART": None,  # Исполнитель альбома (Album Artist) str
                        "\\xa9too": None,  # Программа кодирования (Encoding software) str
                        "\\xa9cmt": None,  # Комментарий (Comment) str
                    }
                }
                counter += 1
        if counter == 1:
            self.update_info_text("В папке нет файлов расширения '.mp3' и .m4a")

        with open(self.audio_list_path, "w", encoding="utf-8") as f:
            json.dump(audio_files, f, ensure_ascii=False, indent=2)

        return audio_files


        # self.update_info_text("Нажата кнопка 2")

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