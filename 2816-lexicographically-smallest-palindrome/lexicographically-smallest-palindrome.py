class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        for i in range(len(s) >> 1): s[i], s[len(s) - 1 - i] = min(s[i], s[len(s) - 1 - i]), min(s[i], s[len(s) - 1 - i])
        return "".join(s)