from typing import List

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a * b) // gcd(a, b)

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        
        for num in nums:
            while st and gcd(st[-1], num) != 1:
                num = lcm(st.pop(), num)
            st.append(num)
        
        return st
