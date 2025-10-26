class Solution:
    def sum(self, num1: int, num2: int) -> int:
        result = 0

        for x in range(abs(num1)): result += (1 * (num1 // abs(num1)))
        for x in range(abs(num2)): result += (1 * (num2 // abs(num2)))

        return result