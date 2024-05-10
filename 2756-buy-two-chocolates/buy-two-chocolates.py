class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        b = money - prices[0] - prices[1]
        if b >= 0:
            return b
        else:
            return money  

        
        