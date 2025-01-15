class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        return int(bin(num1)[:1:-1].replace('1','0',num1.bit_count() - num2.bit_count())[::-1], 2) if num1.bit_count() > num2.bit_count() else int((bin(num1)[:1:-1]+'0'*32).replace('0','1',-num1.bit_count() + num2.bit_count())[::-1], 2)