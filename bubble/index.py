import random
import time

def сортировка_пузырьком(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def сортировка_слиянием(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        сортировка_слиянием(L)
        сортировка_слиянием(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def генерация_случайного_массива(size):
    return [random.randint(0, 1000) for _ in range(size)]

def измерение_времени_сортировки(функция_сортировки, arr):
    start_time = time.time()
    функция_сортировки(arr)
    end_time = time.time()
    return end_time - start_time


размеры_массивов = [1000, 5000, 10000]
for size in размеры_массивов:
    arr = генерация_случайного_массива(size)
    время_выполнения = измерение_времени_сортировки(сортировка_пузырьком, arr)
    print(f"Сортировка пузырьком: Размер массива {size}, Время выполнения: {время_выполнения:.6f} секунд")


for size in размеры_массивов:
    arr = генерация_случайного_массива(size)
    время_выполнения = измерение_времени_сортировки(сортировка_слиянием, arr)
    print(f"Сортировка слиянием: Размер массива {size}, Время выполнения: {время_выполнения:.6f} секунд")
