def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    # if n<m:
    #     arr,brr = brr,arr
    # i = 0
    # arr = ''.join(map(str,arr))
    # brr = ''.join(map(str,brr))
    # while(i<m):
    #     if brr[i:] in arr:
    #         return brr[i:]
    #     if brr[:m-i] in arr:
    #         return brr[:m-i]
    #     else:
    #         i+=1
    # return []
    
    intersection = []
    i = j = 0

    while i < len(arr) and j < len(brr):
        if arr[i] == brr[j]:
            intersection.append(arr[i])
            i += 1
            j += 1
        elif arr[i] < brr[j]:
            i += 1
        else:
            j += 1

    return intersection

arr = [1, 7, 8, 10, 11, 11, 12, 13, 13, 14, 14]
brr = [0, 1, 12, 13, 14]
result = findArrayIntersection(arr, len(arr), brr, len(brr))

print(f"Array One: {arr}\nArray Two: {brr}\nIntersection: {result}")