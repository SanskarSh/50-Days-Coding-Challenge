def maxSubarraySum(arr) :
    temp = 0
    max_val = 0

    for i in arr:
        temp = max(i, temp + i)
        max_val = max(max_val, temp)

    return max_val

arr = [0, 1, 3, 4, 5, 9, 10, 12, 13, -1]
result = maxSubarraySum(arr)

print(f"Array: {arr}\nMax Sum Prossible in Subarray: {result}")