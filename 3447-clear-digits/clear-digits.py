class Solution:
    def clearDigits(self, s: str) -> str:
        st = deque()

        for c in s: 
            if not c.isdigit(): st.append(c)
            else: st.pop()
        
        return "".join(st)

        #return "".join(st := [c for c in s if not c.isdigit()][:-sum(c.isdigit() for c in s)])
