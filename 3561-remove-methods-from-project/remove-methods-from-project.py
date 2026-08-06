class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        ma = defaultdict(list)

        for a, b in invocations: ma[a].append(b)
        
        visited = set()

        def visit(x):
            if x in visited: return
            visited.add(x)
            for b in ma[x]: 
                visit(b)
            return
        
        visit(k)

        for a, b in invocations:
            if a not in visited and b in visited:
                return list(range(n))
        
        return list(set(range(n)) - visited)