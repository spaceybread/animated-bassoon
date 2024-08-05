class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1, w2 = {}, {}

        for a in words1:
            if a in w1:
                w1[a] += 1
            else:
                w1[a] = 1
        
        for a in words2:
            if a in w2:
                w2[a] += 1
            else:
                w2[a] = 1

        c = 0
        for a in w1:
            if w1.get(a) == 1 and w2.get(a) == 1:
                c += 1
        
        return c