def setZeroes(self, matrix: list[list[int]]) -> list[list[int]]:
    rowLen, colLen = len(matrix), len(matrix[0])
    zero_row, zero_col = set(), set()

    for i in range(rowLen):
        for j in range(colLen):
            if(matrix[i][j] == 0):
                zero_row.add(i)
                zero_col.add(j)

    for i in range(rowLen):
        for j in range(colLen):
            if i in zero_row or j in zero_col:
                matrix[i][j] = 0

    return matrix

arr = [[1,1,1],[1,0,1],[1,1,1]]

print(setZeroes(None, arr))
