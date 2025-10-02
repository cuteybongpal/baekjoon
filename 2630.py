N = int(input())
square = []

for i in range(N):
    square.append(list(map(int, input().split())))

#반환값 튜플의 첫번째 원소는 파란색 종이의 개수, 두번째는 하얀색 종이의 개수
def find_square(startX, endX, startY, endY) -> tuple[int, int]:
    sum = 0
    for i in range(startX, endX, 1):
        for j in range(startY, endY, 1):
            sum += square[i][j]
    if sum == (endX - startX)*(endY - startY):
        return (1, 0)
    if sum == 0:
        return (0, 1)
    midX = (startX + endX) // 2
    midY = (startY + endY) // 2
    
    white = 0
    blue = 0
    b, w = find_square(startX, midX, startY, midY)
    white += w
    blue += b
    
    b, w = find_square(midX, endX, startY, midY)
    white += w
    blue += b
    
    b, w = find_square(startX, midX, midY, endY)
    white += w
    blue += b
    
    b, w = find_square(midX, endX, midY, endY)
    white += w
    blue += b
    
    return blue, white
b, w = find_square(0, N, 0, N)
print(w)
print(b)