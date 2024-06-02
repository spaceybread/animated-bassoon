class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) >> 1):
            blah = s[i]
            s[i] = s[-(i + 1)]
            s[-(i + 1)] = blah
        """
        Do not return anything, modify s in-place instead.
        """
        