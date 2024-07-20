class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rs, cs, i, j = len(rowSum), len(colSum), 0, 0
        mat = [[0] * cs for _ in range(rs)]

        while i < rs and j < cs:
            x = min(rowSum[i], colSum[j])
            mat[i][j] = x

            rowSum[i] -= x
            colSum[j] -= x
            
            i += (rowSum[i] == 0)
            j += (colSum[j] == 0)

        
        return mat