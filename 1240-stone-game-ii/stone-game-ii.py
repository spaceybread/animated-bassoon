class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        mat = [[0] * (n + 1) for _ in range(n)]
        sus = [0] * n
        sus[-1] = piles[-1]
        
        for i in range(n - 2, -1, -1):
            sus[i] = sus[i + 1] + piles[i]
        
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    mat[i][m] = sus[i]
                else:
                    for x in range(1, 2 * m + 1):
                        mat[i][m] = max(mat[i][m], sus[i] - mat[i + x][max(m, x)])
        
        return mat[0][1]
