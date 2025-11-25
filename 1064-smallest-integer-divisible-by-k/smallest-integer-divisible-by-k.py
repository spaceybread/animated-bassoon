import sys

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        sys.set_int_max_str_digits(0)
        
        if k % 2 == 0: return -1
        if k % 5 == 0: return -1 

        o = 1

        while True: 
            if o % k == 0: return len(str(o))
            o = 10 * o + 1