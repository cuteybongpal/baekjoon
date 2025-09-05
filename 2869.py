import math
a, b, v = map(int, input().split())


c = (v-b) / (a - b)

if int(c) == c:
    print(int(c))
else:
    print(math.ceil(c))