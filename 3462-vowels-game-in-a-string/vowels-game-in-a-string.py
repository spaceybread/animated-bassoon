class Solution:
    def doesAliceWin(self, s: str) -> bool: 
        return sum([1 if c in "aeiou" else 0 for c in s ]) > 0
        
        