class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        num_ops = 1
        
        while True:
            delta = num1 - num_ops * num2
            if delta < num_ops: return -1

            bdelt = bin(delta)[2:]
            ones = sum([1 if s == '1' else 0 for s in bdelt])

            if num_ops >= ones: return num_ops
            num_ops += 1



