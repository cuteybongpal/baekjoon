def placeQueen(currentQueenCount:int, cols:list, diagonaldown:list, diagonalup:list, count:int):
    c = count
    isSuccessed = False

    for i in range(len(cols)):
        if not cols[i]:
            continue
        if not diagonaldown[i - currentQueenCount + len(cols) - 1]:
            continue
        if not diagonalup[i + currentQueenCount]:
            continue

        cols[i] = False
        diagonaldown[i - currentQueenCount + len(cols) - 1] = False
        diagonalup[i + currentQueenCount] = False

        if (currentQueenCount < len(cols) - 1):
            c = placeQueen(currentQueenCount + 1, cols, diagonaldown , diagonalup, c)

        cols[i] = True
        diagonaldown[i - currentQueenCount + len(cols) - 1] = True
        diagonalup[i + currentQueenCount] = True
        isSuccessed = True
    if isSuccessed and currentQueenCount == len(cols) - 1:
        c += 1
    return c

queenCount = int(input())

row = [True] * queenCount
col = [True] * queenCount
diagonaldown = [True] * (queenCount * 2 - 1)
diagonalup = [True] * (queenCount * 2 - 1)

b = placeQueen(0, col, diagonaldown, diagonalup, 0)
print(b)