a = int(input())
stack = []
result = []
for i in range(a):
    parts = input().split()
    instruction = parts[0]
    value = parts[1] if len(parts) > 1 else None
    
    if instruction == 'push':
        stack.append(int(value))
    if instruction == 'pop':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack.pop())
    if instruction == 'size':
        result.append(len(stack))
    if instruction == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    if instruction == 'top':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])
        
for i in result:
    print(i)