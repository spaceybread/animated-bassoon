class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ss = defaultdict(list)

        if len(s) != len(goal): return False

        for i in range(len(s)):
            ss[s[i]] += [s[i - 1], s[(i + 1) % len(s)]]
        
        out = True 
        for i in range(len(goal)):
            x = goal[i]
            lx, rx = goal[i - 1], goal[(i + 1) % len(goal)]
            aj = ss[x]
            
            hasMatch = False
            for j in range(0, len(aj), 2):
                if lx == aj[j] and rx == aj[j + 1]:
                    hasMatch = True
                    break
            out = out and hasMatch
        
        return out

