a = int(input())
answers = []
for i in range(a):
    b, c = input().split()
    b = int(b)
    res = ''
    for i in c:
        res += i * b
    answers.append(res)

for i in answers:
    print(i)