# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, n, val, path):
        if n.val == val:
            return True
        if n.left and self.find(n.left, val, path):
            path += "L"
        elif n.right and self.find(n.right, val, path):
            path += "R"
        return path


    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        s, d = [], []
        self.find(root, startValue, s)
        self.find(root, destValue, d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))
            