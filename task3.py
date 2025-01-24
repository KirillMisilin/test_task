import random


# Реализация быстрой сортировки
def sort(arr):
    if len(arr) < 2:  # если в массиве 0 или 1 элемент, его не нужно сортировать
        return arr
    sep = arr[random.randint(0, len(arr) - 1)]  # случайный выбор разделителя
    small_arr = [num for num in arr if num < sep]  # создание массива элементов, меньших разделителя
    big_arr = [num for num in arr if num > sep]  # создание массива элементов, больших разделителя
    equal_arr = [num for num in arr if num == sep]  # создание массива элементов, равных разделителю
    return sort(small_arr,) + equal_arr + sort(big_arr)  # возврат отсортированного массива, для small_arr и big_arr
    # запускается рекурсия, пока в них не окажется 0 или 1 элемент