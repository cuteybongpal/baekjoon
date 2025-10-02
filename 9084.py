T = int(input())
res = []

for i in range(T):
    c = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    dp = [0] * (money + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, money + 1):
            dp[x] += dp[x - coin]
    res.append(dp[money])
print("\n".join(map(str, res)))