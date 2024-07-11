class Solution:
    def reverseParentheses(self, s: str) -> str:
        rs = ['']
        for c in s:
            if c == '(':
                rs.append('')
            elif c == ')':
                rs[len(rs) - 2] += rs.pop()[::-1]
            else:
                rs[-1] += c
        return "".join(rs)