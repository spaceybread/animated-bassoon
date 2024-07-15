class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(m)
        for j in range(n):
            for i in range(j + 1, n):
                m[i][j], m[j][i] = m[j][i], m[i][j]

        for j in range(n):
            for i in range(n >> 1):
                m[j][i], m[j][n - i - 1] = m[j][n - i - 1], m[j][i]