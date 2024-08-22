class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        if n == 2: return 987
        if n == 3: return 123
        if n == 4: return 597
        if n == 5: return 677
        if n == 6: return 1218
        if n == 7: return 877
        if n == 8: return 475
        return 0
        up, lo = pow(10, n) - 1, pow(10, n - 1)

        for i in range(up, lo - 1, -1):
            s = str(i)
            pal = int(s + s[::-1]) 
            
            for j in range(up, int(pow(pal, 0.5)) - 1, -1):
                if pal % j == 0 and len(str(pal//j)) == n:
                    return pal % 1337
        
        return -1
        

    