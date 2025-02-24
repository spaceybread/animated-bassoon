class Solution:
    def mostProfitablePath(self, edges: List[List[int]], b: int, amt: List[int]) -> int:
        g = {}
        for u, v in edges:
            if u not in g: g[u] = [v]
            else: g[u].append(v)
            if v not in g: g[v] = [u]
            else: g[v].append(u)

        pt = [0] * len(amt)
        st = [0]

        while st:
            u = st.pop()
            for v in g[u]:
                st.append(v)
                g[v].remove(u)
                pt[v] = u
        
        pa = [b]
        while pt[b] != b:
            pa.append(pt[b])
            b = pt[b]
        
        d = len(pa)
        for i in range(d // 2): amt[pa[i]] = 0 
        if d % 2: amt[pa[d // 2]] >>= 1

        st.append(0)
        out = -999999999999
        while st:
            u = st.pop()
            if g[u]:
                for v in g[u]:
                    st.append(v)
                    amt[v] += amt[u]
            elif out < amt[u]:
                out = amt[u]
        return out