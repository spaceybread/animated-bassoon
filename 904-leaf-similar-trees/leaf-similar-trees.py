# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leaf_set(self, root, se):
        if root.left is None and root.right is None:
            se.append(root.val)
        else:
            if root.left is not None: self.get_leaf_set(root.left, se)
            if root.right is not None: self.get_leaf_set(root.right, se)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1, s2 = [], []
        self.get_leaf_set(root1, s1)
        self.get_leaf_set(root2, s2)

        return s1 == s2