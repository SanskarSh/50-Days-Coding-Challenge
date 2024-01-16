def rotateArray(arr: list, k: int) -> list:
    return arr[k:]+arr[0:k]

arr = [1,2,3,4,5,6,7]
rotateBy = 2
result = rotateArray(arr, rotateBy)

print(f"Array: {arr}\nRotate By: {rotateBy}\nResult: {result}")