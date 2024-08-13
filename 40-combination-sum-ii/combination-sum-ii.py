class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ca = sorted(candidates)
        res, path = [], []

        self.dfs(ca, 0, target, path, res)
        return res
    
    def dfs(self, cand, cur, target, path, res):
        if target==0:
            res.append(path.copy())
            return
        if target < 0:
            return
        
        for i in range(cur, len(cand)):
            if i > cur and cand[i] == cand[i - 1]:
                continue
            path.append(cand[i])
            self.dfs(cand, i+1, target - cand[i], path, res)
            path.pop()