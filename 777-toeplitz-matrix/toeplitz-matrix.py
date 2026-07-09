class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                if i + 1 < n and j + 1 < m:
                    if matrix[j][i] != matrix[j + 1][i + 1]:
                        return False

        return True
