class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_0 = Counter([s1[i] for i in range(0, len(s1), 2)])
        s1_1 = Counter([s1[i] for i in range(1, len(s1), 2)])

        s2_0 = Counter([s2[i] for i in range(0, len(s2), 2)])
        s2_1 = Counter([s2[i] for i in range(1, len(s2), 2)])

        return (s1_0 == s2_0) and (s1_1 == s2_1)