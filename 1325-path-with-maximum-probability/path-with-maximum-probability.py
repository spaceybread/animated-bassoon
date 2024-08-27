class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        d = [0] * n
        d[start_node] = 1

        for ni in range(n - 1):
            flag = True
            for i, (u, v) in enumerate(edges):
                if d[u] * succProb[i] > d[v]: d[v], flag = d[u] * succProb[i], False
                if d[v] * succProb[i] > d[u]: d[u], flag = d[v] * succProb[i], False
            if flag:
                break
        return d[end_node]       