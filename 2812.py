n, cnt = map(int, input().split())
cnt2 = cnt
number = str(input())
Stack = []
index = 0
for i in range(len(number)):
    if cnt == 0:
        Stack.append(number[i])
        continue
    if not Stack:
        Stack.append(number[i])
        continue
    while 1:
        
        if len(Stack) != 0 and Stack[-1] < number[i] and cnt > 0:
            Stack.pop()
            cnt -= 1
        else: break
    Stack.append(number[i])

for i in range(n - cnt2, len(Stack)):
    Stack.pop()
print("".join(map(str, Stack)))
