from sortedcontainers import SortedSet
class NumberContainers:
    def __init__(self):
        self.nti = defaultdict(SortedSet)
        self.itn = defaultdict()

    def change(self, idx: int, n: int) -> None:
        if idx in self.itn:
            temp = self.itn[idx]
            self.nti[temp].discard(idx)
        self.itn[idx] = n
        self.nti[n].add(idx)

    def find(self, n: int) -> int:
        if not self.nti[n]:
            return -1
        return self.nti[n][0]