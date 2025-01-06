class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        out = [0] * n
        pc, ps, sc, ss = 0, 0, 0, 0

        for i in range(n):
            out[i] = pc * i - ps
            if boxes[i] == "1":
                pc += 1
                ps += i
        
        for i in range(n - 1, -1, -1):
            out[i] += ss - sc * i
            if boxes[i] == "1":
                sc += 1
                ss += i
        
        return out