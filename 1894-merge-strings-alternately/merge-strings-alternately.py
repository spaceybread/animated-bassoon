class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        flag = True
        out = ""
        while i < len(word1) and j < len(word2):
            if flag:
                out += word1[i]
                i += 1
                flag = False
            else: 
                out += word2[j]
                j += 1
                flag = True
        
        out += word1[i:]
        out += word2[j:]

        return out