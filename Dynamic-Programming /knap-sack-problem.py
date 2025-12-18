# Profits and weights
profits = [1, 2, 5, 6]
weights = [2, 3, 4, 5]
capacity = 8

def mapsack(weights, profits, capacity):
    n = len(weights)
    
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)] # creating 2d array 


    for i in range(1, n + 1):  
        for w in range(1, capacity + 1):   
            if weights[i-1] <= w: 
                # Item fits → include it or skip it, take max
                dp[i][w] = max(profits[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                # Item too heavy → cannot include, copy previous row
                dp[i][w] = dp[i-1][w]

        print(f"After considering item {i} (weight={weights[i-1]}, profit={profits[i-1]}):")
        print(dp[i])
        print("-" * 50)

    return dp[n][capacity]

max_profit = mapsack(weights, profits, capacity)
print("Maximum profit:", max_profit)
