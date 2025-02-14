class ProductOfNumbers:

    def __init__(self):
        self.li = [1]

    def add(self, num: int) -> None:
        if num == 0: self.li = [1]
        else: self.li.append(self.li[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.li): return 0
        return self.li[-1] // self.li[-(k + 1)]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)