def bubble_sort(cars, key, reverse=False):
    arr = list(cars)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = getattr(arr[j], key)
            val2 = getattr(arr[j + 1], key)
            if (val1 > val2 and not reverse) or (val1 < val2 and reverse):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(cars, key, reverse=False):
    arr = list(cars)
    n = len(arr)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            val1 = getattr(arr[j], key)
            val2 = getattr(arr[idx], key)
            if (val1 < val2 and not reverse) or (val1 > val2 and reverse):
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr

def quick_sort(cars, key, reverse=False):
    arr = list(cars)
    if len(arr) <= 1:
        return arr
    pivot = getattr(arr[len(arr) // 2], key)
    left = [x for x in arr if (getattr(x, key) < pivot and not reverse) or (getattr(x, key) > pivot and reverse)]
    middle = [x for x in arr if getattr(x, key) == pivot]
    right = [x for x in arr if (getattr(x, key) > pivot and not reverse) or (getattr(x, key) < pivot and reverse)]
    return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)