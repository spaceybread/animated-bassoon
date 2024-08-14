class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, l = 0, False
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                l = False
            else:
                i += 1
                l = True
        
        return l
            