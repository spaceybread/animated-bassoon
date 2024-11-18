class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        circ = code + code + code
        if k == 0: return [0] * len(code)

        out = []
        for i in range(len(code), len(code) + len(code)):
            if k > 0:
                out.append(sum(circ[i + 1 : i + k + 1]))
            else:
                out.append(sum(circ[i + k : i]))

        return out