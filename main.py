import os
import timeit
from modules.algorithm import insertion_sort, merge_sort, quicksort, heapsort, sort_data  # Імпортуємо функцію для сортування
from modules.logger import log_action  # Імпортуємо функцію для логування з модуля logger
from modules.visualization import plot_comparison  # Імпортуємо функцію для побудови графіків
from modules.merge_k_lists import merge_k_lists, validate_k_lists  # Імпортуємо функції для злиття списків та перевірки даних
from modules.datasets import generate_and_validate_datasets  # Імпортуємо функцію для генерації та перевірки даних
from modules.heatmap import generate_heatmap  # Імпортуємо функцію для побудови теплової карти
import random
import numpy as np

# Функція для генерації випадкових відсортованих списків для merge_k_lists
def generate_random_k_lists(num_lists=3, list_size_range=(5, 10), value_range=(1, 20)):
    """
    Генерує k відсортованих списків для тестування merge_k_lists.
    
    Параметри:
    num_lists (int): кількість списків для генерації.
    list_size_range (tuple): діапазон для розміру списків.
    value_range (tuple): діапазон для значень елементів списків.
    
    Повертає:
    list: Список відсортованих списків цілих чисел.
    """
    lists = []
    for _ in range(num_lists):
        size = random.randint(*list_size_range)
        data = [random.randint(*value_range) for _ in range(size)]
        lists.append(sorted(data))  # Відсортовані списки
    return lists

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

# Функція для очищення екрану
def clear_screen():
    if os.name == 'nt':  # Для Windows
        os.system('cls')
    else:  # Для Linux / macOS
        os.system('clear')

# Функція для вимірювання часу виконання алгоритму
def measure_time(sort_function, data):
    try:
        start_time = timeit.default_timer()  # Початок вимірювань
        sort_function(data)  # Виконання сортування
        end_time = timeit.default_timer()  # Кінець вимірювань
        return end_time - start_time  # Повертаємо час виконання
    except Exception as e:
        log_action(f"Помилка при вимірюванні часу виконання алгоритму: {e}")
        raise

# Функція для збору статистики
def gather_statistics(times):
    if not times:
        return None
    avg_time = np.mean(times)
    max_time = np.max(times)
    min_time = np.min(times)
    std_dev = np.std(times)
    return {"avg": avg_time, "max": max_time, "min": min_time, "std_dev": std_dev}

# Функція для тестування алгоритмів на різних наборах даних
def test_algorithms():
    try:
        datasets = generate_and_validate_datasets()  # Генерація та перевірка даних
    except ValueError as e:
        log_action(f"Помилка перевірки даних: {e}")
        print(f"Помилка: {e}")
        return

    dataset_descriptions = [
        "Малий набір випадкових чисел",
        "Середній набір випадкових чисел",
        "Набір з випадковими великими числами",
        "Відсортований у зворотному порядку список (1000 елементів)",
        "Вже відсортований набір даних (1000 елементів)"
    ]
    
    times_insertion = []
    times_merge = []
    times_timsort = []
    times_quick = []  # Час для QuickSort
    times_heap = []   # Час для HeapSort

    for idx, data in enumerate(datasets):
        print(f"\n{'='*37}")
        print(f"Тестування для: {dataset_descriptions[idx]}")
        print(f"Набір даних: {data[:5]}...")

        # Порівняння часу виконання кожного алгоритму
        try:
            time_insertion = measure_time(insertion_sort, data.copy())
            time_merge = measure_time(merge_sort, data.copy())
            time_timsort = measure_time(sorted, data.copy())  # Timsort у Python реалізований через sorted()
            time_quick = measure_time(quicksort, data.copy())  # QuickSort
            time_heap = measure_time(heapsort, data.copy())   # HeapSort
        except Exception as e:
            log_action(f"Помилка при виконанні тесту для набору даних: {e}")
            print(f"Помилка при виконанні тесту для набору даних: {e}")
            continue

        times_insertion.append(time_insertion)
        times_merge.append(time_merge)
        times_timsort.append(time_timsort)
        times_quick.append(time_quick)
        times_heap.append(time_heap)

        print("\nЧас виконання алгоритмів:")
        print(f"  - Час сортування вставками: {time_insertion:.6f} сек.")
        print(f"  - Час сортування злиттям: {time_merge:.6f} сек.")
        print(f"  - Час сортування Timsort: {time_timsort:.6f} сек.")
        print(f"  - Час сортування QuickSort: {time_quick:.6f} сек.")
        print(f"  - Час сортування HeapSort: {time_heap:.6f} сек.")

        log_action(f"Тестування на даних {data[:5]}... : Insertion: {time_insertion:.6f}, Merge: {time_merge:.6f}, Timsort: {time_timsort:.6f}, QuickSort: {time_quick:.6f}, HeapSort: {time_heap:.6f}")
        
        stats_insertion = gather_statistics(times_insertion)
        stats_merge = gather_statistics(times_merge)
        stats_timsort = gather_statistics(times_timsort)
        stats_quick = gather_statistics(times_quick)
        stats_heap = gather_statistics(times_heap)

        print("\nСтатистика для сортування вставками:")
        print(f"  - Середній час: {stats_insertion['avg']:.6f} сек.")
        print(f"  - Максимальний час: {stats_insertion['max']:.6f} сек.")
        print(f"  - Мінімальний час: {stats_insertion['min']:.6f} сек.")
        print(f"  - Стандартне відхилення: {stats_insertion['std_dev']:.6f} сек.")

    # Виводимо графік після виконання всіх тестів
    plot_comparison(times_insertion, times_merge, times_timsort, times_quick, times_heap)

    # Генерація випадкових даних для merge_k_lists
    print("\n=== Тестування злиття кількох відсортованих списків ===")
    k_lists = generate_random_k_lists()  # Генеруємо випадкові списки

    # Перевіряємо коректність даних
    try:
        validate_k_lists(k_lists)  # Перевірка згенерованих даних
    except ValueError as e:
        log_action(f"Помилка перевірки даних для merge_k_lists: {e}")
        print(f"Помилка перевірки даних для merge_k_lists: {e}")
        return

    print(f"Згенеровані відсортовані списки: {k_lists}")
    
    try:
        print("Виконання злиття списків...")
        merged_list = merge_k_lists(k_lists)
        print(f"\nОб'єднаний відсортований список з k списків: {merged_list}")
    except Exception as e:
        log_action(f"Помилка при об'єднанні списків: {e}")
        print(f"Помилка при об'єднанні списків: {e}")

    # Генерація теплової карти
    generate_heatmap([times_insertion, times_merge, times_timsort, times_quick, times_heap])

def print_ascii_art():
    ascii_art = """
    =======================================
    =        Порівняння алгоритмів        =
    =    Сортування вставками, злиттям    =
    =    та Timsort за часом виконання   =
    =======================================
    """
    print(ascii_art)

def main():
    clear_screen()
    print_ascii_art()
    print("=== Початок тестування алгоритмів ===")
    test_algorithms()
    print("=== Завершення виконання скрипта ===")
    log_action("Порівняння алгоритмів сортування вставками, злиттям та Timsort завершено.")

if __name__ == "__main__":
    main()
