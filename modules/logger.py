import os
from datetime import datetime

# Шлях до файлу для збереження логів
log_file = 'logs/log.txt'

# Функція для логування дій
def log_action(action):
    # Отримуємо поточну дату і час
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Відкриваємо файл для додавання нової інформації
    with open(log_file, 'a') as file:
        file.write(f"[{current_time}] {action}\n")  # Записуємо дату, час і дію у файл
    
    print(f"Логування виконано: [{current_time}] {action}")  # Виводимо дію на екран
