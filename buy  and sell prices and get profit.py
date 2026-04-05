class solution:
    def maxProfit(prices):
        max_profit=0
        min_price=float('inf')
        for price in prices:
            if price<min_price:
                min_price=price
            else:
                Profit=price-min_price
                if Profit>max_profit:
                    max_profit=Profit
        return max_profit
    print(maxProfit([7,1,3,5,6]))