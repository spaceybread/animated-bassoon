class Solution:
    def isCircularSentence(self, se: str) -> bool:
        se = se.split()
        se = [se[-1]] + se + [se[0]]

        for i in range(len(se) - 1):
            if se[i][-1] != se[i + 1][0]: return False
        
        return True