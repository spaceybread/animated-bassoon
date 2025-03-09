class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        out, c = 0, 1
        colors.extend(colors[0 : k - 1])
        for c1, c2 in pairwise(colors):
            if c1 == c2:
                out += max(0, c - k + 1)
                c = 1
                continue
            c += 1
        return out + max(0, c - k + 1)
