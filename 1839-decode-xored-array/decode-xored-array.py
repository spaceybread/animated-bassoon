class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        out = [first] + encoded

        for i in range(len(encoded)):
            out[i + 1] = out[i] ^ out[i + 1]   

        return out 