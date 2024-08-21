class Solution:
    def strangePrinter(self, s: str) -> int:
        return self.h(0, len(s)-1, s, [[-1] * len(s) for _ in range(len(s))])

    def h(self, i, j, s, dp):
        if i > j: return 0
        if dp[i][j] != -1: return dp[i][j]

        first_letter = s[i]
        answer = 1 + self.h(i + 1, j, s, dp)
        for k in range(i + 1, j + 1):
            if s[k] == first_letter:          
                better_answer = self.h(i, k - 1, s, dp) + self.h(k + 1, j, s, dp)
                answer = min(answer, better_answer)
        dp[i][j] = answer
        return answer
