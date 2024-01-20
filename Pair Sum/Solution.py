def pairSum(arr, n, target):
    seen = set()
    count = 0

    for num in arr:
        complement = target - num

        if complement in seen:
            count += 1

        seen.add(num)

    return count if count > 0 else -1

arr = (1, 2, 3, 4, 5, 6, 7, 8, 9)
target = 6
result = pairSum(arr, len(arr), target)

print(f"Nuber of pairs in the Array: {arr}\nWhose are of target: {target}\n Are: {result}")