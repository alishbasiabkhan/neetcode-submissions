class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0

        for right in range(1, len(prices)):
            # print('left:', left, 'right:', right, 'prices[left]:', prices[left], 'prices[right]:', prices[right])
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                print('profit:', profit)
                max_profit = max(max_profit, profit)
            else:
                left = right
        return max_profit
        