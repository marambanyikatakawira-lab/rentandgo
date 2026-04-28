def linear_search(cars, key, value):
    results = []
    for car in cars:
        if str(getattr(car, key)).lower() == str(value).lower():
            results.append(car)
    return results

def binary_search(cars, key, value):
    arr = sorted(cars, key=lambda x: str(getattr(x, key)).lower())
    low, high = 0, len(arr) - 1
    results = []
    value = str(value).lower()
    
    while low <= high:
        mid = (low + high) // 2
        mid_val = str(getattr(arr[mid], key)).lower()
        if mid_val == value:
            results.append(arr[mid])
            l, r = mid - 1, mid + 1
            while l >= 0 and str(getattr(arr[l], key)).lower() == value:
                results.insert(0, arr[l])
                l -= 1
            while r < len(arr) and str(getattr(arr[r], key)).lower() == value:
                results.append(arr[r])
                r += 1
            break
        elif mid_val < value:
            low = mid + 1
        else:
            high = mid - 1
    return results