posX, posY, sizeX, sizeY = map(int, input().split())

dist = [ posX, posY, sizeX - posX, sizeY - posY]

min = posX
for i in dist:
    if (i < min):
        min = i

print(min)
