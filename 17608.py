a = int(input())
stack = []

for i in range(a):
    val = int(input())
    
    if len(stack) == 0:
        stack.append(val)
        continue
    
    while True:
        if len(stack) == 0:
            break
        if stack[len(stack)-1] <= val:
            stack.pop()
        else:
            break
    stack.append(val)
print(stack)
print(len(stack))