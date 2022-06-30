def maxProfit(self, prices):
    global min_price
    max_profit = 0
    min_price = prices[0]
    for i in range(len(prices) - 1):
        if prices[i] < min_price:
            min_price = prices[i]
        tot = prices[i + 1] - min_price
        if max_profit < tot:
            max_profit = tot

    return max_profit