class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        out = []
        for n in nums:
            ns = [int(x) for x in str(n)]
            for i in range(len(ns)):
                ns[i] = mapping[ns[i]]

            x = 0
            for a in ns:
                x = x*10 + a

            out.append((x, n))
        
        out.sort(key=lambda x: x[0])
        outln = []

        for b, c in out:
            outln.append(c)
        
        return outln
