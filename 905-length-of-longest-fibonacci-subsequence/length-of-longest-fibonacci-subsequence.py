class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        se = set(arr)
        out = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a, b = arr[i], arr[j]
                l = 2

                while a + b in se:
                    a, b = b, a + b
                    l += 1

                if l > 2 and l > out:
                    out = l

        return out