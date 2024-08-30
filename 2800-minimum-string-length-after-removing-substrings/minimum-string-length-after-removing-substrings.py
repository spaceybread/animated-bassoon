class Solution:
    def minLength(self, s: str) -> int:
        c = 0
        while "AB" in s or "CD" in s:
            s = list(s)

            for i in range(1, len(s)):
                if s[i - 1] == "A" and s[i] == "B" or s[i - 1] == "C" and s[i] == "D":
                    s[i - 1], s[i] = "", ""
                    c += 1
            s = "".join(s)

        return len(s)