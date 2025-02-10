class Solution:
    def clearDigits(self, s: str) -> str:
        st = deque()

        for c in s: 
            if not c.isdigit(): st.append(c)
            else: st.pop()
        
        return "".join(st)