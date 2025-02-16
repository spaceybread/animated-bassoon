class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        def f(idx = 0): 
            if not u: return True
            if a[idx]: return f(idx+1)
            for nu in reversed(range(1,n+1)):
                id = idx + nu if nu != 1 else idx
                if nu in u and id < 2*n - 1 and not a[id]:
                    a[idx] = a[id] = nu
                    u.remove(nu)
                    if f(idx+1): return True
                    a[idx] = a[id] = 0
                    u.add(nu)
            return False

        a, u = [0]*(2*n - 1), set(range(1,n+1))
        f()

        return a