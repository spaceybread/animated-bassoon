class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mp = [-2] * 32
        mp[0] = -1

        ml, m = 0, 0

        for i, char in enumerate(s):
            if char == 'a': m ^= 1 
            if char == 'e': m ^= 2 
            if char == 'i': m ^= 4 
            if char == 'o': m ^= 8 
            if char == 'u': m ^= 16

            p = mp[m]
            if p == -2: mp[m] = i
            else: ml = max(ml, i - p)
        
        return ml