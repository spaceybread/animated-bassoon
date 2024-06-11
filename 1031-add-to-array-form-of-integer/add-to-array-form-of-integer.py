class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for a in num:
            n = n*10 + a
        
        print(n)
        n += k
        print(n)

        sys.set_int_max_str_digits(9999 + 9999)
        n = list(str(n))
        
        for i in range(len(n)):
            n[i] = int(n[i])

        return n