def insertionSort(n: int, arr) -> None:
    for i in range(n):
        if i < n-1 and arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            if(len(arr[:i+1])>1):
                temp = arr[i+1:]
                arr[:] = insertionSort(len(arr[:i+1]),arr[:i+1]) + temp
        if i == n-1:
            return arr

    # for i in range(n):
    #     while i > 0 and arr[i] < arr[i-1]:
    #         arr[i], arr[i-1] = arr[i-1], arr[i]
    #         i -= 1
    # return arr

arr = [4, 34, 44, 32, 19, 32, 11, 11, 29, 46, 9]
result = insertionSort(len(arr), arr)

print(f"Array: {arr}\nArray sorted using Insertion Sort: {result}")