a = int(input())

per = []

for i in range(a):
    b, *scores = map(int, input().split())
    mean = 0
    sum = 0
    for i in scores:
        sum += i
    mean = sum / len(scores)
    c = 0
    for i in scores:
        if mean < i:
            c += 1
    per.append(c / len(scores) * 100)

for i in per:
    print(f"{i:.3f}%")