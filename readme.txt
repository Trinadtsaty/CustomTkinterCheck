Создаём виртуальное окружение (venv):
    python -m venv venv

Активируем виртуальное окружение:
    Windiws:
    venv\Scripts\activate

    Linux/Mac:
    source venv/bin/activate

Установите библиотеки из requirements.txt:
    pip install -r requirements.txt

Деактивация venv:
    deactivate

Проверка установленных библиотек:
    pip list

Экспортируйте список библиотек в requirements.txt
    pip freeze > requirements.txt

self - это ссылка на сам объект (наше окно).
После super().__init__() наш объект self становится полноценным окном CustomTkinter,
поэтому мы можем вызывать все методы CTk через self.

