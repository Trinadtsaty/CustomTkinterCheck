import customtkinter as ctk


# 1. Класс для красной кнопки
class RedButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        # Вызываем конструктор родительского класса (CTkButton)
        super().__init__(
            master=master,
            text="Красная кнопка",
            fg_color="#ff4444",  # Основной цвет - красный
            hover_color="#cc3333",  # Цвет при наведении - темно-красный
            text_color="white",  # Цвет текста - белый
            command=self.on_click,  # Привязываем метод обработки
            **kwargs  # Передаем дополнительные аргументы
        )

    def on_click(self):
        print("Это красная кнопка!")


# 2. Класс для желтой кнопки
class YellowButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(
            master=master,
            text="Желтая кнопка",
            fg_color="#ffcc00",  # Основной цвет - желтый
            hover_color="#cc9900",  # Цвет при наведении - темно-желтый
            text_color="black",  # Цвет текста - черный (лучше видно на желтом)
            command=self.on_click,
            **kwargs
        )

    def on_click(self):
        print("Это желтая кнопка!")


# 3. Класс для зеленой кнопки
class GreenButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(
            master=master,
            text="Зеленая кнопка",
            fg_color="#44ff44",  # Основной цвет - зеленый
            hover_color="#33cc33",  # Цвет при наведении - темно-зеленый
            text_color="white",
            command=self.on_click,
            **kwargs
        )

    def on_click(self):
        print("Это зеленая кнопка!")


class DynamicButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        self._command = kwargs.pop('command', None)
        super().__init__(master, command=self._execute, **kwargs)

    def set_command(self, new_command):
        """Изменяет команду кнопки динамически"""
        self._command = new_command

    def _execute(self):
        """Выполняет текущую команду"""
        if self._command:
            self._command()