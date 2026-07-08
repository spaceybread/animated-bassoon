class Solution:
    def sumAndMultiply(self, s: str, a: List[List[int]]) -> List[int]:
        M = 10**9 + 7

        def co(acc, d):
            if d == 0: return acc
            return (acc * 10 + d) % M

        ds = list(map(int, s))
        ps = list(accumulate(ds, co, initial=0))

        kong = list(accumulate((c > '0' for c in s), initial=0))
        pss = list(accumulate(ds, initial=0))

        o = []
        for l, r in a:
            bing = kong[r + 1] - kong[l]
            fn = (ps[r + 1] - ps[l] * pow(10, bing, M)) % M
            ds = pss[r + 1] - pss[l]
            o.append(fn * ds % M)

        return o