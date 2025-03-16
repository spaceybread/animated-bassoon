class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        a = range(cars**2 * max(ranks))
        f = lambda t: sum(isqrt(t // r) for r in ranks)
        return bisect_left(a, cars, key = lambda t: f(t))
