class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(), s2.split()
        sa = set()
        r = set()

        for w in s1:
            if w in sa:
                sa.remove(w)
                r.add(w)
            else:
                if w not in r:
                    sa.add(w)
        
        for w in s2:
            if w in sa:
                sa.remove(w)
                r.add(w)
            else:
                if w not in r:
                    sa.add(w)
        
        return list(sa)