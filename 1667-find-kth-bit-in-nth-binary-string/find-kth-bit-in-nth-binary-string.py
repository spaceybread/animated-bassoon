class Solution:
    def inv(self, s):
        return "".join(["0" if x == "1" else "1" for x in list(s)])

    def findKthBit(self, n: int, k: int) -> str:
        s = "0"

        for _ in range(n - 1): s += "1" + self.inv(s)[::-1]

        return s[k - 1]