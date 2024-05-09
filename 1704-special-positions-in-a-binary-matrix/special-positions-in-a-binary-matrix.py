class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        c = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    t = True
                    for k in range(1, len(mat)):
                        if mat[(i + k) % len(mat)][j] == 1:
                            t = False
                    for k in range(1, len(mat[i])):
                        if mat[i][(j + k) % len(mat[i])] == 1:
                            t = False
                    if t:
                        c += 1
        return c
            