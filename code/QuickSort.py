def quick_sort(arr):
    arr = arr[:]
    def _quick(a, low, high):
        if low < high:
            p = partition(a, low, high)
            _quick(a, low, p - 1)
            _quick(a, p + 1, high)
    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1
    _quick(arr, 0, len(arr) - 1)
    return arr

if __name__ == "__main__":
    print(quick_sort([10, 7, 8, 9, 1, 5]))