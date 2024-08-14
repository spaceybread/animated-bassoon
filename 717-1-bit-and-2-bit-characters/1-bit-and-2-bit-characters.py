class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, l = 0, 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                l = 1
            else:
                i += 1
                l = 0
        
        return l == 0
            