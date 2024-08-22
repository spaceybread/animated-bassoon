class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9

        up, lo = pow(10, n) - 1, pow(10, n - 1)

        for i in range(up, lo - 1, -1):
            s = str(i)
            pal = int(s + s[::-1]) 
            
            for j in range(up, int(pow(pal, 0.5)) - 1, -1):
                if pal % j == 0 and len(str(pal//j)) == n:
                    return pal % 1337
        
        return -1
        

    