def bubbleSort(arr,n):
    while(True):
        count = True
        for index in range(0, n):
            if(index+1 == n):
                if(count):
                    return arr
                continue
            else:
                if(index+1 == n):
                    continue
                if(arr[index] > arr[index+1]):
                    count = False
                    temp = arr[index]
                    arr[index] = arr[index+1]
                    arr[index+1] = temp

# def bubbleSort(arr, n):
#     for i in range(n):
#         isSorting = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 isSorting = True
#         if not isSorting:
#             break

#     return arr

arr = [7, 33, 24, 25, 3, 13, 34, 47, 50, 33, 37, 18, 36, 12]
result = bubbleSort(arr, len(arr))

print(f"Array: {arr}\nArray sorted using Bubble Sort: {result}")