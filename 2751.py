import sys

a = int(sys.stdin.readline())
ls = []
for i in range(a):
    ls.append(int(sys.stdin.readline()))

ls.sort()

for i in ls:
    print(i)