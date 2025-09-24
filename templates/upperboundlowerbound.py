def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

# Example usage:
arr = [1, 2, 4, 4, 4, 5, 6, 7]
target = 4
print("Lower bound:", lower_bound(arr, target))  # Output: 2
print("Upper bound:", upper_bound(arr, target))  # Output: 5
def lower_bound_lr(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def upper_bound_lr(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Example usage:
print("Lower bound (l <= r):", lower_bound_lr(arr, target))  # Output: 2
print("Upper bound (l <= r):", upper_bound_lr(arr, target))  # Output: 5