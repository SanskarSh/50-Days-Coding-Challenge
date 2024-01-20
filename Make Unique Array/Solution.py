def minElementsToRemove(arr):
    unique_elements = set()
    count = 0
    for i in arr:
        if i in unique_elements:
            count += 1
        else:
            unique_elements.add(i)
    return count

arr = (13, 15, 12, 1, 1, 14, 4, 2, 19, 11)
result = minElementsToRemove(arr)

print(f"In order to make the array {arr} unique you need to remove {result} items.")