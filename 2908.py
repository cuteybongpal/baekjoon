a, b = map(str, input().split())

san_a = ''
san_b = ''

for i in range(len(a)- 1, -1, -1):
    san_a += a[i]
 
for i in range(len(b)- 1, -1, -1):
    san_b += b[i]

if (int(san_a) > int(san_b)):
    print(san_a)
else:
    print(san_b)