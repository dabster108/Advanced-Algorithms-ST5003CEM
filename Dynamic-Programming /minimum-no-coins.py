def coin_change(coins, target):
    n = len(coins)
    INF = float('inf')
    dp = [[INF] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
        for j in range(1, target + 1):
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Min of excluding or including the coin
                dp[i][j] = min(
                    dp[i - 1][j],                 # exclude coin
                    1 + dp[i][j - coins[i - 1]]   # include coin (unlimited)
                )

    return dp[n][target] if dp[n][target] != INF else -1

if __name__ == "__main__":
    coins = [1, 2,5]
    target = 6

    result = coin_change(coins, target)

    if result != -1:
        print(f"Minimum coins needed: {result}")
    else:
        print("Target cannot be formed with given coins")
