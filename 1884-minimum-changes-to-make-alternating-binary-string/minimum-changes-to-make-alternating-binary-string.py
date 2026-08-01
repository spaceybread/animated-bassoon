class Solution:
    def minOperations(self, s: str) -> int:
        return min(sum([1 & (ord(s[i]) ^ i) for i in range(len(s))]), len(s) - sum([1 & (ord(s[i]) ^ i) for i in range(len(s))]))
