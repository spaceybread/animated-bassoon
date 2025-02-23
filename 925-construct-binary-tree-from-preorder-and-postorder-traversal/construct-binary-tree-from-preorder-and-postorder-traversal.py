# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, pe, po):

        node = TreeNode(po.pop())
        if node.val != pe[-1]: node.right = self.f(pe, po)
        if node.val != pe[-1]: node.left = self.f(pe, po)
        pe.pop()

        return node


    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.f(preorder, postorder)
