class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        li = []

        for line in mat:
            for j in line:
                li.append(j)
        
        out = []
        con = 0
        for i in range(r):
            out.append([])
            for j in range(c):
                out[i].append(li[con])
                con += 1
        return out
