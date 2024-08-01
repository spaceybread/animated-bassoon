class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for a in details:
            if int(a[len(a) - 4:len(a) - 2]) > 60:
                c += 1 
        
        return c