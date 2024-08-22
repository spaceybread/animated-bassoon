class Solution:
    def findComplement(self, num: int) -> int:
        x = int(math.log2(num)) + 1
  
        for i in range(x):  
            num = (num ^ (1 << i))  
      
        return num