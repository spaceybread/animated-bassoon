from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.numberToIndices = defaultdict(SortedSet)
        self.indexToNumber = defaultdict()

    def change(self, index: int, number: int) -> None:
        if index in self.indexToNumber:
            temp = self.indexToNumber[index]
            self.numberToIndices[temp].discard(index)
        self.indexToNumber[index] = number
        self.numberToIndices[number].add(index)

    def find(self, number: int) -> int:
        if not self.numberToIndices[number]:
            return -1
        else:
            return self.numberToIndices[number][0]