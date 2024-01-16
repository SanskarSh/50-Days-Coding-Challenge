def findSecondLargest(arr):
    temp = sorted(list(set(arr)))
    return temp[len(temp)-2] if(len(temp)>1) else -1

arr = [1,2,3,4,5,6,7,8,8]
result = findSecondLargest(arr)
print(f"\nArray: {arr}\nSecond Largest Value: {result}")