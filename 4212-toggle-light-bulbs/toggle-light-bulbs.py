class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        return sorted(list(set([x for x in bulbs if Counter(bulbs)[x] % 2 == 1])))