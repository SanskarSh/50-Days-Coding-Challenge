def selectionSort(arr,n):
    for i in range(n):
        pivot = i
        for j in range(n):
            if arr[pivot] < arr[j]:
                arr[pivot], arr[j] = arr[j], arr[pivot]
    return arr


arr = [4, 34, 44, 32, 19, 32, 11, 11, 29, 46, 9]
result = selectionSort(arr, len(arr))

print(f"Array: {arr}\nArray sorted using Selection Sort: {result}")