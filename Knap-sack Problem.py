def knapsack(W, wt, val, n):
    # Initialize the DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                # Max of (including the item) vs (excluding the item)
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                )
            else:
                # Item is too heavy, carry forward the previous max
                dp[i][w] = dp[i - 1][w]
                
    return dp[n][W] # Moved outside the loops

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print("Maximum value:", knapsack(W, wt, val, n))52.0