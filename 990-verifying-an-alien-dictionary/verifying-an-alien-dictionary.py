class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        if n == 1:
            return True
        d = {}
        for i in range(len(order)):
            d[order[i]] = i
        
        for i in range(n - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                
                if words[i][j] != words[i + 1][j]:
                    if d[words[i][j]] > d[words[i + 1][j]]:
                        return False
                    break
        return True