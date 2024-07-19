class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minL = [10^5 + 1] * len(matrix)
        maxL = [-1] * len(matrix[0])

        for j in range(len(matrix)):
            l = matrix[j]
            for i in range(len(l)):
                if l[i] > maxL[i]:
                    maxL[i] = l[i]
            minL[j] = min(l)

        sol = []

        for a in minL:
            if a in maxL:
                sol.append(a)
        
        return sol