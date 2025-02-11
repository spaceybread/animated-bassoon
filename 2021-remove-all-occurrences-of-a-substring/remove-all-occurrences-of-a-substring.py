class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s: s = re.sub(re.escape(part), '', s, 1)
        return s
