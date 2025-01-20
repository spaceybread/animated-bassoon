class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ids = sorted(range(len(mat[0])*len(mat)), key = lambda x: arr[x])
        return min([max([ids[mat[i][j] - 1] for i in range(len(mat))]) for j in range(len(mat[0]))] + [max([ids[mat[i][j] - 1] for j in range(len(mat[0]))]) for i in range(len(mat))])