class Solution:
    def toHex(self, num: int) -> str:
        return hex(num)[2:] if num >= 0 else hex(num + 2**32)[2:]