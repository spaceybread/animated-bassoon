class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ls = title.split()
        s = []

        for si in ls:
            if len(si) > 2:
                s.append(si.title())
            else:
                s.append(si.lower())
        
        return " ".join(s)