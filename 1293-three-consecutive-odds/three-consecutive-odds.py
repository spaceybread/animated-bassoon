class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c = 0

        for a in arr:
            if a % 2 == 0:
                c = 0
            else:
                c += 1

                if c > 2:
                    return True

        return False