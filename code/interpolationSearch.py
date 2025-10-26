def interpolation_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi and arr[lo] != arr[hi]:
        pos = lo + ((hi - lo) * (target - arr[lo])) // (arr[hi] - arr[lo])
        if pos < lo or pos > hi:
            break
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1
    if lo < len(arr) and arr[lo] == target:
        return lo
    return -1

if __name__ == "__main__":
    print(interpolation_search([10, 20, 30, 40, 50, 60, 70, 80], 50))