import time
import logging
from functools import wraps

# 1. Декоратор для измерения времени выполнения
def timer_decorator(func):
    @wraps(func)  # сохраняем метаданные оригинальной функции
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time:.4f} секунд")
        return result
    return wrapper


# 2. Декоратор для проверки атрибутов функции
def validate_attributes_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Проверяем, есть ли у функции атрибуты
        if not args and not kwargs:
            print(f"Функция {func.__name__} вызвана без аргументов - выполнение прервано")
            return None

        # Проверяем конкретные типы аргументов (пример проверки)
        for arg in args:
            if arg is None:
                print(f"Функция {func.__name__} получила None в аргументах - выполнение прервано")
                # logging.warning(f"Функция {func.__name__} получила None в аргументах - выполнение прервано")
                return None

        for key, value in kwargs.items():
            if value is None:
                print(f"Функция {func.__name__} получила None в аргументе {key} - выполнение прервано")
                # logging.warning(f"Функция {func.__name__} получила None в аргументе {key} - выполнение прервано")
                return None

        # Если все проверки пройдены, выполняем функцию
        return func(*args, **kwargs)

    return wrapper