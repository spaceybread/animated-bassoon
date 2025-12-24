class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        a = sum(apple)
        c = sorted(capacity)[::-1]
        i = 0

        while i < len(c) and a > 0:
            b =  min(c[i], a)
            c[i] -= b
            a -= b
            if a == 0: return i + 1
            i += 1
        
        return i
            