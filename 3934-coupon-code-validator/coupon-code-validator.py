class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        bl = ["electronics", "grocery", "pharmacy", "restaurant"]
        def check(s):
            if s == '': return False
            for x in s: 
                if x.lower() not in 'abcdefghijklmnopqrstuvwxyz1234567890_':
                    print('rejected', s)
                    return False
            return True
        
        ma = {}
        for b in bl: ma[b] = []

        for i in range(len(code)):
            if businessLine[i] not in bl: 
                print('rejected bl', businessLine[i])
                continue

            if isActive[i] and check(code[i]): ma[businessLine[i]].append(code[i])

        o = []
        for b in bl: o += sorted(ma[b])
        return o