# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sol(self, r, o):
        if r:
            self.sol(r.left, o)
            self.sol(r.right, o)
            o.append(r.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.sol(root, out)
        return out
        