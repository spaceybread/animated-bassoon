class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m = Counter(list(moves))
        return m['U'] == m['D'] and m['L'] == m['R']