class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mop = {}
        for a in range(len(heights)):
            mop[heights[a]] = names[a]
        
        h = sorted(heights)[::-1]
        
        sol = []

        for a in h:
            sol.append(mop[a])
        
        return sol
