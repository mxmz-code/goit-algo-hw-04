import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import os

def plot_comparison(times_insertion, times_merge, times_timsort, times_quick, times_heap):
    """
    Створює графік порівняння часу виконання різних алгоритмів сортування.
    
    Параметри:
    times_insertion (list): Час виконання для сортування вставками.
    times_merge (list): Час виконання для сортування злиттям.
    times_timsort (list): Час виконання для сортування Timsort.
    times_quick (list): Час виконання для сортування QuickSort.
    times_heap (list): Час виконання для сортування HeapSort.
    """
    
    # Перевірка, що всі елементи в списках times є числами
    times = [times_insertion, times_merge, times_timsort, times_quick, times_heap]
    
    for time_list in times:
        if not all(isinstance(time, (int, float)) for time in time_list):
            raise ValueError("Всі елементи в списках часу повинні бути числами.")
    
    # Дані для побудови графіка (використовуємо середнє значення для кожного алгоритму)
    labels = ['Insertion Sort', 'Merge Sort', 'Timsort', 'QuickSort', 'HeapSort']
    times = [
        sum(times_insertion)/len(times_insertion),
        sum(times_merge)/len(times_merge),
        sum(times_timsort)/len(times_timsort),
        sum(times_quick)/len(times_quick),
        sum(times_heap)/len(times_heap)
    ]

    # Побудова стовпчикового графіка
    plt.bar(labels, times, color=['blue', 'green', 'red', 'purple', 'orange'])
    plt.ylabel('Час виконання (сек.)')
    plt.title('Порівняння часу виконання алгоритмів сортування')
    
    # Отримуємо поточну дату і час у форматі YYYY-MM-DD_HH-MM-SS
    current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    # Формуємо назву файлу з поточною датою та часом
    file_path = f"graph/comparison_time_{current_datetime}.png"
    
    # Збереження графіка перед його закриттям
    plt.savefig(file_path)  # Зберігаємо графік
    
    plt.show()  # Виведення графіка на екран
    
    plt.close()  # Закриваємо графік після збереження і відображення
    print(f"Графік порівняння часу виконання алгоритмів збережений в {file_path}")

def generate_heatmap(time_data, filename="heatmap"):
    """
    Генерує теплову карту для порівняння часу виконання алгоритмів.
    
    Параметри:
    time_data (list of lists): Список з часами виконання для кожного алгоритму.
    filename (str): Базове ім'я файлу для збереження теплової карти (без розширення).
    """
    # Перетворення часу виконання в масив NumPy для побудови теплової карти
    data = np.array(time_data)

    # Створення теплової карти
    plt.figure(figsize=(10, 6))
    sns.heatmap(data, annot=True, cmap="YlGnBu", fmt=".6f", xticklabels=["Insertion", "Merge", "Timsort", "QuickSort", "HeapSort"], yticklabels=["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4", "Dataset 5"])
    
    plt.title("Теплова карта часу виконання алгоритмів сортування")
    plt.xlabel("Алгоритми сортування")
    plt.ylabel("Типи даних")

    # Створюємо папку "graph", якщо вона не існує
    if not os.path.exists('graph'):
        os.makedirs('graph')

    # Отримуємо поточну дату і час у форматі YYYY-MM-DD_HH-MM-SS
    current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Формуємо назву файлу з поточною датою та часом
    file_path = f"graph/{filename}_{current_datetime}.png"

    # Зберігаємо теплову карту
    plt.savefig(file_path)
    
    plt.show()  # Виведення теплової карти на екран
    
    plt.close()  # Закриваємо графік після збереження і відображення
    print(f"Теплова карта збережена в {file_path}")
