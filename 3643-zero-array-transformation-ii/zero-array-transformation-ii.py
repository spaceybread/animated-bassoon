class Solution:
    def f(self, q, k, nums):
        n, rs = len(nums), 0
        di = defaultdict(int)

        for i in range(k):
            di[q[i][0]] += q[i][2]
            di[q[i][1]+1] -= q[i][2]

        for i in range(n):
            rs += di[i]
            if rs < nums[i]: return False 

        return True 

    def minZeroArray(self, nums: List[int], qs: List[List[int]]) -> int:
        l, r = 0, len(qs)

        while l <= r:
            m = ( l + r ) // 2 
            if self.f(qs, m, nums): r = m - 1 
            else: l = m + 1 

        return l if l <= len(qs) else -1