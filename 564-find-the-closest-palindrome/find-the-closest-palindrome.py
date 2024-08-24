class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == '1': return "0"

        l, can = len(n), set()
        pre = n[:(l + 1) // 2]
        pren = int(pre)

        for i in [-1, 0, 1]:
            np = str(pren + i)
            if l % 2 == 0:
                c = np + np[::-1]
            else:
                c = np + np[:-1][::-1]
            can.add(c)

        can.add(str(10**(l-1) - 1))
        can.add(str(10**l + 1))
        can.discard(n)

        cp = min(can, key = lambda x: (abs(int(x) - int(n)), int(x)))

        return cp
