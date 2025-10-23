import time
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
    def wrapper(self, *args, **kwargs):
        print("Декоратор начал выполнение")

        # Проверяем атрибут external_command экземпляра
        if hasattr(self, 'external_command'):
            if callable(self.external_command):
                print("external_command является функцией")
                return func(self, *args, **kwargs)
            else:
                print("external_command не является функцией")
                # Но ВСЕ РАВНО выполняем оригинальную функцию!
                return func(self, *args, **kwargs)
        else:
            print("Атрибут external_command не найден")
            return func(self, *args, **kwargs)  # Все равно выполняем

    return wrapper