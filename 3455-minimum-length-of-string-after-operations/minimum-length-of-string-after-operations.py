from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if c % 2 == 1 else 2 for c in Counter(s).values())