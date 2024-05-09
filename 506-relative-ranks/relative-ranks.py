class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        place = sorted(score)[::-1]

        build = []
        for a in score: 
            n = place.index(a)

            if n == 0:
                build.append("Gold Medal")
            elif n == 1:
                build.append("Silver Medal")
            elif n == 2:
                build.append("Bronze Medal")
            else:
                build.append(str(n + 1))

        return build