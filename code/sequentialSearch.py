def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

if __name__ == "__main__":
    print(linear_search([3, 5, 2, 7, 9, 1, 4], 7))