class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig = [0] + digits
        c = 1
        for i in range(len(dig) - 1, -1, -1):
            x = dig[i] + c
            if x % 10 == x: 
                dig[i] = x
                break
            else: 
                dig[i] = x % 10
                c = 1
        
        if dig[0] == 0: return dig[1:]
        else: return dig
