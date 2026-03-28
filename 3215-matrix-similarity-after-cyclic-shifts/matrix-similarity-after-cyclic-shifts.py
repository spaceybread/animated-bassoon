class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        ll = k % len(mat[0])
        if ll == 0: return True

        flag = True
        for i in range(len(mat)):
            x = mat[i]
            y = x[ll:] + x[:ll]
            if i % 2 == 1: y = x[-1 * ll:] + x[:-1 * ll]
            flag = flag and (x == y)

        return flag