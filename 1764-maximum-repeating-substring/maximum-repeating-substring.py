class Solution:
    def maxRepeating(self, s: str, word: str) -> int:
        
        k, ma, tm = 0, 0, word
        while tm in s:
            k += 1
            tm += word
            ma = max(ma, k)
        
        return ma