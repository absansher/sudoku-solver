problema = [
           [1, 0, 8, 0, 0, 4, 0, 0, 0],
           [0, 6, 0, 7, 0, 8, 2, 1, 9],
           [3, 9, 0, 0, 1, 0, 7, 0, 0],
           [0, 0, 3, 6, 0, 0, 4, 7, 2],
           [0, 8, 0, 4, 5, 9, 0, 6, 0],
           [6, 1, 4, 0, 0, 3, 5, 0, 0],
           [0, 0, 9, 0, 6, 0, 0, 4, 7],
           [7, 4, 1, 3, 0, 5, 0, 2, 0],
           [0, 0, 0, 1, 0, 0, 9, 0, 5]]
M = 9
def solve(problema, row, col, num):
    for x in range(9):
        if problema[row][x] == num:
            return False

    for x in range(9):
        if problema[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if problema[i + startRow][j + startCol] == num:
                return False
    return True

def Bajar(problema, row, col):
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if problema[row][col] > 0:
        return Bajar(problema, row, col + 1)
    for num in range(1, M + 1, 1):

        if solve(problema, row, col, num):

            problema[row][col] = num
            if Bajar(problema, row, col + 1):
                return True
        problema[row][col] = 0
    return False

def final(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()

if (Bajar(problema, 0, 0)):
    final(problema)
else:
    print("Laqqa tushding, Net resheniy!")
