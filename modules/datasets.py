import random

def generate_and_validate_datasets(num_lists=5, list_size_range=(5, 20), value_range=(0, 100)):
    """
    Функція для генерації та перевірки випадкових наборів даних.
    Генерує k відсортованих списків і перевіряє їх на коректність.
    
    Параметри:
    num_lists (int): кількість списків для генерації.
    list_size_range (tuple): діапазон для розміру списків.
    value_range (tuple): діапазон для значень елементів списків.
    
    Повертає:
    list: Список відсортованих списків цілих чисел.
    """
    datasets = []
    
    try:
        # Генерація випадкових відсортованих списків
        for _ in range(num_lists):
            size = random.randint(*list_size_range)
            data = [random.randint(*value_range) for _ in range(size)]
            datasets.append(sorted(data))  # Відсортовані списки
        
        # Перевірка на правильність даних
        validate_datasets(datasets)
    
    except (TypeError, ValueError) as e:
        raise ValueError(f"Помилка при генеруванні чи перевірці даних: {e}")
    
    return datasets

def validate_datasets(datasets):
    """
    Перевірка правильності структури та елементів списків.
    
    Параметри:
    datasets (list): Список списків для перевірки.
    
    Викидає:
    TypeError, ValueError якщо дані некоректні.
    """
    if not isinstance(datasets, list):
        raise TypeError("Дані повинні бути списком списків.")
    
    for i, dataset in enumerate(datasets):
        if not isinstance(dataset, list):
            raise TypeError(f"Набір даних на індексі {i} повинен бути списком.")
        if not all(isinstance(x, int) for x in dataset):
            raise ValueError(f"Набір даних на індексі {i} містить нецілі числа.")
        if not dataset:  # Перевірка на порожні списки
            raise ValueError(f"Набір даних на індексі {i} порожній.")
    
    return True
