class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {'(':')', '[':']', '{':'}'}

        for i in range(len(s)):
            if s[i] in d:
                st.append(s[i])
            elif len(st) == 0 or s[i] != d[st.pop()]:
                return False
        
        return len(st) == 0

               
