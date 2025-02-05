class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c2 = Counter(s2)

        for s in list(s1):
            if c2.get(s) != None:
                c2[s] -= 1
            else: return False
        
        for s in list(s2):
            if c2.get(s) != 0: return False

        hd = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]: hd += 1
        

        return hd == 0 or hd == 2
