
# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Алгоритм QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Алгоритм HeapSort
def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Функція для сортування даних різними алгоритмами
def sort_data(arr, algorithm="insertion"):
    """
    Функція для сортування даних різними алгоритмами.
    
    Параметри:
    arr (list): Список для сортування.
    algorithm (str): Алгоритм сортування ("insertion", "merge", "quicksort", "heapsort").
    
    Повертає:
    list: Відсортований список.
    """
    if algorithm == "insertion":
        return insertion_sort(arr)
    elif algorithm == "merge":
        return merge_sort(arr)
    elif algorithm == "quicksort":
        return quicksort(arr)
    elif algorithm == "heapsort":
        return heapsort(arr)
    else:
        raise ValueError(f"Невідомий алгоритм: {algorithm}")
