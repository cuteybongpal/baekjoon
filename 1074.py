def move(x:int, y:int, size:int, N:int, index:int, desX:int, desY:int):  
    if N > 1:
        if desY < x - (size**0.5 // 2) and desX < y - (size**0.5 // 2):
            move(x - (size**0.5 // 2),y - (size**0.5 // 2), size//4, N-2, index - 3 * (2 ** N), desX, desY)
        
        elif desY >= x - (size**0.5 // 2) and desX < y - (size**0.5 // 2):
            move(x ,y - (size**0.5 // 2), size//4, N-2, index - 2 * (2 ** N), desX, desY)
        
        elif desY < x - (size**0.5 // 2) and desX >= y - (size**0.5 // 2):
            move(x - (size**0.5 // 2), y, size//4, N-2, index - 1 * (2 ** N), desX, desY)
        
        elif desY >= x - (size**0.5 // 2) and desX >= y - (size**0.5 // 2):
            move(x, y, size//4, N-2, index - 0 * (2 ** N), desX, desY)
    else:
        if desX == y - 2 and desY == x - 2:
            print(int(index) - 4)
        elif desX == y - 2 and desY == x - 1:
            print(int(index) - 3) 
        elif desX == y - 1 and desY == x - 2:
            print(int(index) - 2)
        elif desX == y - 1 and desY == x - 1:
            print(int(index) - 1)

nn, dx, dy = map(int,input().split())
move(2**nn,2**nn,(2**nn) * (2**nn), 2 * (nn - 1), (2**nn) * (2**nn), dx, dy)