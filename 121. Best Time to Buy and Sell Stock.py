class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = float('inf')
        best = 0
        for price in prices:
            if least > price:
                least = price
            if price - least > best:
                best = price - least
        return best



        