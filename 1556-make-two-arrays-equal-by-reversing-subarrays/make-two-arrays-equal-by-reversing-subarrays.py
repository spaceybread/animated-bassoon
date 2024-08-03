class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        from collections import Counter
        if Counter(target) == Counter(arr):
            return True
        return False