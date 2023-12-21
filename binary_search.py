# Binary search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 10

result = binary_search(sorted_arr, target_value)

if result != -1:
    print(f"Targte value {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the array.")
