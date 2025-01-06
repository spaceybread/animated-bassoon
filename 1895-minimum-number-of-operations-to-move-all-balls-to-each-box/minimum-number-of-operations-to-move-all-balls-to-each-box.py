class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ne = []
        
        for i in range(len(boxes)):
            if boxes[i] == "1": ne.append(i)
        
        out = []

        for i in range(len(boxes)):
            s = 0
            for a in ne:
                s += abs(a - i)
            out.append(s)
        
        return out