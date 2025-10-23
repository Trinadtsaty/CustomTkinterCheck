import customtkinter as ctk
from .decorator import validate_attributes_decorator

# 1. Класс для красной кнопки
class CustomButton(ctk.CTkButton):
    def __init__(self, master, text="Красная кнопка",fg_color="#ff4444",hover_color="#cc3333", text_color="white", command=None, **kwargs):
        super().__init__(
            master=master,
            text=text,
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            command=self._on_click,
            **kwargs
        )
        self.external_command = command

    @validate_attributes_decorator
    def _on_click(self):
        """Наш универсальный обработчик клика"""
        # 1. Всегда выполняем нашу логику
        print("CustomButton: Кнопка нажата!")

        # 2. Выполняем пользовательскую команду если она есть
        if callable(self.external_command):
            self.external_command()
        else:
            print("Не передано")