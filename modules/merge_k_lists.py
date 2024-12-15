# Функція для злиття кількох відсортованих списків
def merge_k_lists(lists):
    """
    Об'єднує k відсортованих списків у один відсортований список.
    
    Параметри:
    lists (list of lists): Список з кількох відсортованих списків.
    
    Повертає:
    list: Один відсортований список, що містить всі елементи з усіх вхідних списків.
    """
    result = []
    while lists:
        # Знаходимо найменший елемент серед усіх списків
        min_value = min(lists, key=lambda x: x[0] if x else float('inf'))  # Порівнюємо перші елементи
        if min_value:
            result.append(min_value.pop(0))  # Додаємо найменший елемент
        if not min_value:  # Якщо список порожній, видаляємо його
            lists.remove(min_value)
    return result

# Функція для перевірки згенерованих списків
def validate_k_lists(lists):
    """
    Перевіряє, чи є всі елементи цілими числами, чи списки не порожні.
    
    Параметри:
    lists (list): Список з кількома відсортованими списками.
    
    Повертає:
    bool: True, якщо дані коректні, False - якщо є помилки.
    """
    if not isinstance(lists, list):
        raise TypeError("Дані повинні бути списком списків.")
    
    for i, lst in enumerate(lists):
        if not isinstance(lst, list):
            raise TypeError(f"Набір даних на індексі {i} повинен бути списком.")
        if not all(isinstance(x, int) for x in lst):
            raise ValueError(f"Набір даних на індексі {i} містить нецілі числа.")
        if not lst:  # Перевірка на порожні списки
            raise ValueError(f"Набір даних на індексі {i} порожній.")
    
    return True
