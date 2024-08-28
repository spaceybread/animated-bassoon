class Solution:
    def largestOddNumber(self, num: str) -> str:
        n, a = len(num), len(num) - 1
        while a >= 0 and int(num[a]) % 2 == 0: a += -1
        if a < 0: return ""
        return num[:a + 1]