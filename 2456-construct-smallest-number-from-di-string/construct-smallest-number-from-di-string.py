class Solution:
    def smallestNumber(self, pattern: str) -> str:
        out, st = "", []

        for i, c in enumerate(pattern + "I", start = 1):
            st.append(str(i))
            while st and c == "I": out += st.pop()
        
        return out