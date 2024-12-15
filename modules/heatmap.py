import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import os

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
