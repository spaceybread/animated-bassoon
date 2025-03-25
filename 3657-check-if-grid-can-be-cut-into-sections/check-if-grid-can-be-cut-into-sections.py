class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        li = []
        for rect in rectangles:
            li.append((rect[0], 1))
            li.append((rect[2], 0))

        li.sort()
        out, c = 0, 1
        for i in range(1, len(li) - 1):
            if li[i][1] == 1: c += 1
            else: c += -1
            if c == 0: out += 1
        
        if out >= 2: return True
        
        li = []
        for rect in rectangles:
            li.append((rect[1], 1))
            li.append((rect[3], 0))

        li.sort()
        out, c = 0, 1
        for i in range(1, len(li)-1):
            if li[i][1] == 1: c += 1
            else: c += -1
            if c == 0: out += 1
        
        return out >= 2