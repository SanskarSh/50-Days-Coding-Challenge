def search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

arr = [0, 1, 3, 4, 5, 9, 10, 12, 13, -1]
target = 10
result = search(arr, target)

print(f"Array: {arr}\nTarget: {target}\nFound using Binary Search at index: {result}")