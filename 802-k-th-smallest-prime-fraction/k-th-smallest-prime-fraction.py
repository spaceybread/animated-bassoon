class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        r = sorted(arr)
        d = {}
        li = []
        for i in range(len(r)):
            for j in range(i + 1, len(r)):
                ou = r[i] / r[j]
                d[ou] = [r[i], r[j]]
                li.append(ou)
        
        li.sort()        
        #print(li)
        return d[li[k - 1]]


