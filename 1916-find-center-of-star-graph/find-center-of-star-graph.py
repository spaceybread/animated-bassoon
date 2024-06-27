class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a = edges[0]

        if a[0] in edges[1]:
            return a[0]
        else:
            return a[1]