from typing import List

def pascalTriangle(n : int) -> List[List[int]]:

    pascalTri = [[1]]

    for i in range(1, n):
        pascalTri.append([1])

        for j in range(1,i):
            pascalTri[i].append(pascalTri[i-1][j-1] + pascalTri[i-1][j])

        pascalTri[i].append(1)

    return pascalTri

pascal_Triangle: List = pascalTriangle(5)

print("Pascal's Triangle: ")
for i in pascal_Triangle:
    print(*i)
