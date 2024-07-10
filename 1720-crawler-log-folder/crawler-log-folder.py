class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c = 0
        for a in logs:
            if a[0] == '.':
                if a[1] == '.':
                    if c > 0:
                        c -= 1
            else:
                c += 1

        return c