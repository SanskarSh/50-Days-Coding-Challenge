def firstMissing(arr, n):
    arr = sorted(i for i in arr if i >0)
    if not arr or arr[0] > 1:
        return 1
    temp = 1
    for i in arr:
        if i == temp:
            temp += 1
    return temp

arr = (-40, -39, -46, -38, -13, -30, -26, -28, -37, -36)
resule = firstMissing(arr, len(arr))

print(f"Array: {arr}\nFirst Missing Value: {result}")