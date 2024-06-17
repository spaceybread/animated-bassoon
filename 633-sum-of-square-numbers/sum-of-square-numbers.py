class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 1 or c == 0:
            return True

        ma = {}

        for i in range(c):
            if i**2 > c:
                break
            ma[i**2] = 1

            if (c - i**2) in ma.keys():
                return True

        return False