class Solution:
    def sortVowels(self, s: str) -> str:
        vow = []
        s = list(s)

        for c in s:
            if c.lower() in 'aeiou':
                vow.append(c)
 
        vow = sorted(vow)

        j = 0
        for i in range(len(s)):
            if s[i].lower() in 'aeiou':
                s[i] = vow[j]
                j += 1
        
        return "".join(s)