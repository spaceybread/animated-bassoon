class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ma = {"a" : "bc", "b" : "ac", "c" : "ab"}
        q = collections.deque(["a", "b", "c"])

        while (len(q[0])) != n:
            p = q.popleft()
            for nl in ma[p[-1]]:
                q.append(p + nl)
            
        return '' if len(q) < k else q[k - 1]
        