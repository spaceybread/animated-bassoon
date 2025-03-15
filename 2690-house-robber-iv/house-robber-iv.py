class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def f(cap):
            rc, flag = 0, True
            for a in nums:
                if not flag: flag = True 
                elif a <= cap:
                    rc += 1
                    flag = False
                    
            return rc >= k 

        li = list(sorted(set(nums))) 
        l, r = 0, len(li) - 1 

        while l < r: 
            m = (l + r) // 2
            if f(li[m]): r = m 
            else: l = m + 1 
        return li[l] 