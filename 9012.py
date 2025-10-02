a = int(input())
result = []
for i in range(a):
    b = input()
    stack = []
    
    isFailed = False
    for j in b:
        if j == '(':
            stack.append('1')
        elif j == ')':
            if len(stack) == 0:
                result.append('NO')
                isFailed = True
                break
            else:
                stack.pop()
    if len(stack) == 0 and not isFailed:
        result.append('YES')
    elif not isFailed:
        result.append('NO')

for i in result:
    print(i)