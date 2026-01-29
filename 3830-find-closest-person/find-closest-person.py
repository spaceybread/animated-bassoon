class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return 1 if abs(z - y) > abs(z - x) else (2 if abs(z - y) < abs(z - x) else 0)