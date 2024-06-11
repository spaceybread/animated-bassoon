class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for ni in arr2:
            d[ni] = 0
        
        r = []
        for n in arr1:
            if n in arr2:
                d[n] += 1
            else:
                r.append(n)
        
        r.sort()
        out = []

        for ni in arr2:
            for c in range(d[ni]):
                out.append(ni)
        
        return out + r