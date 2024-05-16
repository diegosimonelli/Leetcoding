def maxProfit(prices):
    l = 0 # Buy
    r = 1 # Sell
    maxP = 0

    while r < len(prices):
        # we want to check if profitable ?
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP



prices = [7,1,5,3,6,4]
print(maxProfit(prices))