import sys

a = int(sys.stdin.readline())
ls = [0] * 10000
for i in range(a):
    ls[int(sys.stdin.readline())-1] += 1

for i in range(len(ls)):
    for j in range(ls[i]):
        print(f"{i+1}")