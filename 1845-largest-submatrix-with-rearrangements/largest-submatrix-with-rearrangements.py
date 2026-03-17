class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        a = [0] * len(matrix[0])
        out = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: a[j] = 0
                else: a[j] += 1
            
            b = sorted(a)[::-1]
            
            for k in range(len(matrix[0])): out = max(out, b[k] * (k + 1))
        
        return out