a = int(input())
stack = []

for i in range(a):
    val = int(input())
    
    if val == 0:
        stack.pop()
    else:
        stack.append(val)
        
print(sum(stack))
