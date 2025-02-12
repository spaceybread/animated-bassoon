class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ma = {}
        for n in nums:
            s = sum(int(d) for d in str(n))

            if s in ma:
                ma[s].append(n)
            else:
                ma[s] = [n]
        
        m = -1
        
        for k in ma.keys():
            if len(ma[k]) > 1:
                a = sorted(ma[k])

                if a[-1] + a[-2] > m:
                    m = a[-1] + a[-2]

        return m