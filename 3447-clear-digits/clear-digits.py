class Solution:
    def clearDigits(self, s: str) -> str:
        ls = list(s)

        for i in range(len(ls)):
            if ls[i].isdigit():
                for j in range(i, -1, -1):
                    if not ls[j].isdigit() and ls[j] != "":
                        ls[j] = ""
                        break
                ls[i] = ""
        
        return "".join(ls)