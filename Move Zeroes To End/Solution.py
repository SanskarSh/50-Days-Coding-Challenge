def pushZerosAtEnd(arr):
    temp = []
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            arr.pop(i)
            temp.append(0)
    arr+=temp
    return arr

arr = [0, 1, 3, 4, 5, 9, 10, 12, 13, -1]
result = pushZerosAtEnd(arr)

print(f"Array: {arr}\nModified Arrat: {result}")