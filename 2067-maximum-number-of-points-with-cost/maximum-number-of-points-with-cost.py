class Solution:
    def maxPoints(self, m: List[List[int]]) -> int:
        r, c=len(m), len(m[0])
        for i in range(1, r):
            ri=[0]*c
            ri[-1]=m[i-1][-1]
            for j in range(c-2, -1, -1):
                ri[j]=max(ri[j+1]-1, m[i-1][j])
            
            le=m[i-1][0]
            m[i][0]=max(le, ri[0])+m[i][0]
            for j in range(1, c):
                le=max(le-1, m[i-1][j])
                m[i][j]=max(le, ri[j])+m[i][j]
                
        return max(m[-1])