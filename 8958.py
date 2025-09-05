a = int(input())
scores = []
for i in range(a):
    b = input()
    score = 0
    sequencescore = 0
    for j in b:
        f = 0
        if j == 'O':
            f = sequencescore + 1
            sequencescore += 1
        else:
            sequencescore = 0
        score += f
    scores.append(score)

for i in scores:
    print(i)
