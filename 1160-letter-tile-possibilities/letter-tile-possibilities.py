class Solution:
    @cache
    def sol(self, st):
        se, p = set(), 0

        for i, c in enumerate(st): 
            if c in se: continue
            se.add(c)
            p += 1 + self.sol(st[:i] + st[i + 1:])
        
        return p


    def numTilePossibilities(self, tiles: str) -> int: return self.sol(tiles)