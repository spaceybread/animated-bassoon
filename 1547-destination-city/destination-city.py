class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}

        for p in paths: 
            d[p[0]] = p[1]
        
        s = paths[0][0]
        while True:
            if d.get(s) == None:
                return s
            else:
                s = d[s]


        