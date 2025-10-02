import sys
a = int(sys.stdin.readline())

b = list(map(int, sys.stdin.readline().split()))
#단조 스택 사용
#이 문제는 왼쪽부터 값을 비교해가는 문제라서 단조 스택을 사용해야 하는 듯.
#원래 했던 코드의 문제는 최악의 경우 O(N^2) 시간 복잡도를 가지기 때문에 단조 시간 초과가 떴었음
#분명 알고는 있었는데 단조 스택으로 연결이 안됐음 이건 많이 풀다 보면 해결이 될듯함
ddd = []
mono_stack = []
for i in range(a):
    if i == 0:
        mono_stack.append((b[i], i))
        ddd.append(0)
        continue
    # print(mono_stack)
    while len(mono_stack) != 0 and mono_stack[-1][0] < b[i]:
        mono_stack.pop()
        
    if len(mono_stack) == 0:
        ddd.append(0)
    else:
        ddd.append(mono_stack[-1][1]+1)
    mono_stack.append((b[i], i))
    
sys.stdout.write(' '.join(map(str, ddd)))